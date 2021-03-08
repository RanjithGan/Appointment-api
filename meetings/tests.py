from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Meet

class MeetingTests(APITestCase):

    def test_post(self):
        url = "/list/"
        data = {"id":1,"doctor":"x","patient":"b","meeting_date":"2021-05-08"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Meet.objects.get().doctor, 'x')
    
    def test_repeated(self):
        url = "/list/"
        data = {"id":1,"doctor":"x","patient":"b","meeting_date":"2021-05-08"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = {"id":1,"doctor":"x","patient":"b","meeting_date":"2021-05-08"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get(self):
        url = "/list/"
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

