from cmd import IDENTCHARS
from django.db import models

# Create your models here.

class Ticket(models.Model):
    Number = models.IntegerField()
    Value = models.FloatField()
    

    def __str__(self):
        return str(self.Number)

    class Meta:
        verbose_name_plural = "Ticket"


    