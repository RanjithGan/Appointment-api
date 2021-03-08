from django.shortcuts import render
from rest_framework import viewsets
from .models import Meet
from .serializers import MeetSerializer
from rest_framework.validators import ValidationError


# Create your views here.
class MeetApi(viewsets.ModelViewSet):

    queryset = Meet.objects.all()
    serializer_class = MeetSerializer

    def create(self, request):
        pair_list = Meet.objects.filter(doctor=request.data.get("doctor"),patient=request.data.get("patient"))

        for obj in pair_list:
            if (str(obj.doctor) == str(request.data.get("doctor")) and str(obj.patient) == str(request.data.get("patient")) and str(obj.meeting_date) == str(request.data.get("meeting_date"))):
                raise ValidationError('You already have an appointment on that day')
        else:
            return super().create(request)
            
    
    