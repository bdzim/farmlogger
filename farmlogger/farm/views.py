from rest_framework import viewsets

from farmlogger.farm.models import Event
from farmlogger.farm.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
