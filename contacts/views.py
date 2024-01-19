from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.

from .models import Contract, Subcontractor    
from .serializers import ContractSerializer, SubcontractorSerializer

class ContractList(ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class ContractDetail(RetrieveUpdateDestroyAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class SubcontractorList(ListCreateAPIView):
    queryset = Subcontractor.objects.all()
    serializer_class = SubcontractorSerializer

class SubcontractorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Subcontractor.objects.all()
    serializer_class = SubcontractorSerializer