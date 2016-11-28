from rest_framework import viewsets
import pytz
from django.utils.dateparse import parse_datetime

from farmlogger.farm.models import Event, Field, User
from farmlogger.farm.serializers import (
    EventSerializer, FieldSerializer, UserSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class FieldViewSet(viewsets.ModelViewSet):
    serializer_class = FieldSerializer
    queryset = Field.objects.all()


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned events by filtering against query
        parameters in the URL.

        Query parameters:
            user_id (int): The ID of the user who created the event.
            timestamp__gt (Datetime string): Only return events created after this time.
            timestamp__lt (Datetime string): Only return events created before this time.

        TODO:
            * Handle invalid values for query parameters
        """
        queryset = Event.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id:
            user_id = int(user_id)
            queryset = queryset.filter(user__id=user_id)
        timestamp_gt = self.request.query_params.get('timestamp_gt', None)
        if timestamp_gt:
            timestamp_gt = pytz.timezone('UTC').localize(parse_datetime(timestamp_gt))
            queryset = queryset.filter(timestamp__gt=timestamp_gt)
        timestamp_lt = self.request.query_params.get('timestamp_lt', None)
        if timestamp_lt:
            timestamp_lt = pytz.timezone('UTC').localize(parse_datetime(timestamp_lt))
            queryset = queryset.filter(timestamp__lt=timestamp_lt)
        return queryset
