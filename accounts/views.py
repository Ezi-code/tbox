from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from accounts.models import AccountHolder
from accounts.serializers import AccountHolderSerializer
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.response import HTTPResponse


# Create your views here.
class RegisterView(ListCreateAPIView):
    queryset = AccountHolder.objects.all()
    serializer_class = AccountHolderSerializer


class LoginView(APIView):
    
    def post(self, request):
        # print(request.data["email"])
        username = request.data["username"]
        password = request.data["password"]
        user = authenticate(AccountHolder, email=username, password=password)
        serializer = AccountHolderSerializer(data=user)
        if user:
            login(user)
            return Response(serializer.data)

        return Response("")
