from cmd import IDENTCHARS
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Ticket(models.Model):
    eventID = models.IntegerField(null=True)
    Number = models.IntegerField()
    Price = models.FloatField(null=True)
    QR = models.CharField(max_length=200, null=True)
    Picture = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return str(self.Number)

    class Meta:
        verbose_name_plural = "Ticket"    