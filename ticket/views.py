from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import (
   Ticket
)
from .serializers import (
    TicketSerializer
)

class TicketViewset(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
