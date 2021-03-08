from django.db import models
from datetime import date


# Create your models here.
class Meet(models.Model):

    doctor = models.CharField(max_length=100)
    patient = models.CharField(max_length=100)
    meeting_date = models.DateField( default= date.today() )

    def __str__(self):
        return self.doctor + " meeting " + self.patient
    
