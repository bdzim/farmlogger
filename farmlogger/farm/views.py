from rest_framework import viewsets
import pytz
from django.utils.dateparse import parse_datetime

from farmlogger.farm.models import Event
from farmlogger.farm.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned events by filtering against query
        parameters in the URL.
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
