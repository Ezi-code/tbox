from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer, SubcontractorSerializer
from contacts.models import Subcontractor
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView


# Create your views here.
class ProjectList(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# class ProjectSubcontractorView(ListCreateAPIView):
#     serializer_class = SubcontractorSerializer
#     queryset = Subcontractor.objects.all()

#     def get_queryset(self):
#         data = Subcontractor.objects.all()
#         serializer = SubcontractorSerializer(data, many=True)
#         return serializer.data

#     def update(self, request, *args, **kwargs):
#         project = Project.objects.get(pk=kwargs["pk"])
#         subcontractor = Subcontractor.objects.get(pk=request.data["sub_contractor"])
#         project.sub_contractor.set(subcontractor)
#         serializer = ProjectSerializer(project)
#         return serializer.data


# class ProjectSubcontractorView(generics.GenericAPIView):
#     serializer_class = SubcontractorSerializer
#     queryset = Subcontractor.objects.all()


#     def get(self, request, *args, **kwargs):
#         data = Subcontractor.objects.all()
#         serializer = SubcontractorSerializer(data, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
# project = Project.objects.get(pk=kwargs['pk'])
# subcontractor = Subcontractor.objects.get(pk=request.data['sub_contractor'])
#         project.sub_contractor.update(subcontractor)
#         return Response(ProjectSerializer(project).data)


class ProjectSubcontractorView(APIView):
    serializer_class = SubcontractorSerializer
    queryset = Subcontractor.objects.all()



class SeacrProjectView(APIView):
    serializer_class = ProjectSerializer

    def get(self, request):
        print(request.GET.get)
        if request.GET.search:
            data = Project.objects.filter(name=request.GEt.search)
            return data
        data = Project.objects.all()
        return super().get_queryset()
    