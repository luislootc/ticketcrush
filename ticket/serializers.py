from rest_framework import serializers

from .models import (
    EventCategory,
    Event,
    Ticket,
)

class EventCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EventCategory
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = '__all__'
        
class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'