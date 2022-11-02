from rest_framework.decorators import api_view
from rest_framework.response import Response

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
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    serializer_class = EventCategorySerializer
    queryset = EventCategory.objects.all()
    
class EventViewset(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class TicketViewset(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()


# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         'http://localhost/api/v1/'
#     ]

#     return Response(routes)
