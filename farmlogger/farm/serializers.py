from rest_framework import serializers
import logging

from farmlogger.farm.models import (
    Event, User, Field
)

LOG = logging.getLogger(__file__)


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = (
            'id',
            'created_by',
            'name',
            'acres',
            'planted_by',
            'planting_time',
            'crop',
            'total_rainfall',
            'last_rainfall',
            'fertilized_by',
            'fertilizer_type',
            'fertilization_time',
        )


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'timestamp', 'event', 'entity')

    def validate(self, data):
        if data['event'] in ['field:update', 'field:delete',
                             'fertilizing:create', 'planting:create']:
            id_ = data['entity'].get('field_id', data['entity']['id'])
            if not Field.objects.filter(pk=id_).exists():
                LOG.error('Field does does exist with data: {}'.format(data))
                raise serializers.ValidationError(
                    'Field {} does not exist'.format(id_))
        if 'user_id' in data['entity'] or data['event'] == 'user:delete':
            id_ = data['entity'].get('user_id', data['entity']['id'])
            user = User.objects.get(pk=id_)
            if user.deleted:
                LOG.error('User does does exist with data: {}'.format(data))
                raise serializers.ValidationError(
                    'Attempting to perform action with deleted user id: {}'.format(user.pk))
        return data

    def create_user(self, entity):
        return User.objects.create(
            id=int(entity['id']),
            name=entity['name'],
            email=entity['email'],
        )

    def delete_user(self, entity):
        user = User.objects.get(pk=entity['id'])
        user.deleted = True
        user.save()
        return user

    def create_field(self, entity, user):
        return Field.objects.create(
            id=entity['id'],
            created_by=user,
            name=entity['name'],
            acres=entity['acres'],
        )

    def update_field(self, entity):
        field = Field.objects.get(pk=entity['id'])
        field.acres = entity['acres']
        field.name = entity['name']
        field.save()

    def fertilize_field(self, event, entity, user):
        print('test')
        field = Field.objects.get(pk=entity['field_id'])
        print('test2')
        field.fertilizer_type = entity['type']
        field.fertilization_time = event['timestamp']
        field.fertilized_by = user
        field.save()

    def plant_field(self, event, entity, user):
        field = Field.objects.get(pk=entity['field_id'])
        field.crop = entity['crop']
        field.planting_time = event['timestamp']
        field.planted_by = user
        field.save()

    def rainfall(self, event, entity):
        for id_ in entity['fields']:
            field = Field.objects.get(pk=id_)
            field.total_rainfall += entity['amount']
            field.last_rainfall = entity['end']
            field.save()

    def _process_event(self, event):
        entity = event['entity']
        user = None
        if 'user_id' in entity:
            user = User.objects.get(pk=entity['user_id'])
        if event['event'] == 'user:create':
            user = self.create_user(entity)
        elif event['event'] == 'user:delete':
            user = self.delete_user(entity)
        elif event['event'] == 'field:create':
            self.create_field(entity, user)
        elif event['event'] == 'field:update':
            self.update_field(entity)
        elif event['event'] == 'field:delete':
            Field.objects.get(pk=entity['id']).delete()
        elif event['event'] == 'fertilizing:create':
            self.fertilize_field(event, entity, user)
        elif event['event'] == 'planting:create':
            self.plant_field(event, entity, user)
        elif event['event'] == 'rainfall':
            self.rainfall(event, entity)
        return user

    def create(self, validated_data):
        LOG.debug('Event: {}'.format(validated_data))
        user = self._process_event(validated_data)
        return Event.objects.create(
            user=user,
            timestamp=validated_data['timestamp'],
            event=validated_data['event'],
            entity=validated_data['entity'],
        )
