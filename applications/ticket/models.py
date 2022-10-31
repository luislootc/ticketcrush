from cmd import IDENTCHARS
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class EventCategory(models.Model):
    Status = models.CharField(max_length=100, null=True)
    Name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.Name)

    class Meta:
        verbose_name_plural = "EventCategory"
        
class Event(models.Model):
    Name = models.CharField(max_length=100, null=True)
    Description = models.CharField(max_length=300, null=True)
    creationDate = models.DateTimeField()
    expiredDate = models.DateTimeField()
    active = models.BooleanField()
    status = models.CharField(max_length=100, null=True)
    Picture = models.CharField(max_length=200, null=True)
    ticketQty = models.IntegerField()
    CategoryID = models.ForeignKey(EventCategory,on_delete=models.CASCADE)
    YouTubeLink = models.CharField(max_length=250, null=True)
    
    def __str__(self):
        return str(self.Name)

    class Meta:
        verbose_name_plural = "Event"
        
class Ticket(models.Model):
    eventID = models.ForeignKey(Event,on_delete=models.CASCADE)
    Number = models.IntegerField()
    Price = models.FloatField(null=True)
    QR = models.CharField(max_length=200, null=True)
    Picture = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return str(self.Number)

    class Meta:
        verbose_name_plural = "Ticket"