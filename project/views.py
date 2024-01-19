from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Project
from .serializers import ProjectSerializer,SubcontractorSerializer
from contacts.models import Subcontractor
from rest_framework.response import Response
# Create your views here.
class ProjectList(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectSubcontractorView(RetrieveUpdateDestroyAPIView):
    serializer_class = SubcontractorSerializer

    def get_queryset(self):
        return Subcontractor.objects.all()
    

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.save()
        serializer = ProjectSerializer(data=instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
