from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import (
    EventCategory,
    Event,
    Ticket
)
from .serializers import (
    EventCategorySerializer,
    EventSerializer,
    TicketSerializer
)

class EventCategoryViewset(viewsets.ModelViewSet):
    serializer_class = EventCategorySerializer
    queryset = EventCategory.objects.all()
    
class EventViewset(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class TicketViewset(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
