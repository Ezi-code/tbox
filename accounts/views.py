from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView
from accounts.models import AccountHolder
from accounts.serializers import UserSerializer
from django.contrib.auth import login, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response


# from rest_framework.response import HTTPResponse

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponse('You are logged in as {}'.format(user))
    return HttpResponse('You are logged in as')


# Create your views here.
class RegisterView(ListCreateAPIView):
    queryset = AccountHolder.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    
    def post(self, request):
        serializer = UserSerializer.login(data=request.data)
        serializer.is_valid(raise_exception=True) 
        return Response("User logged in successfully", status=200)
    
