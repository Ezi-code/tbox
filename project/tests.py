from django.test import TestCase
from django.urls import reverse, reverse_lazy
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Project
from .serializers import ProjectSerializer
from django.contrib.auth.models import User

# Create your tests here.
class ProjectTests(APITestCase):
    def test_view_projects(self):
        url = reverse_lazy('project-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    