from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.

from .models import Contract    
from .serializers import ContractSerializer

class ContractList(ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class ContractDetail(RetrieveUpdateDestroyAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
