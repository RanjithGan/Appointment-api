from django.shortcuts import render
from rest_framework import viewsets
from .models import Meet
from .serializers import MeetSerializer

# Create your views here.
class MeetApi(viewsets.ModelViewSet):

    queryset = Meet.objects.all()
    serializer_class = MeetSerializer