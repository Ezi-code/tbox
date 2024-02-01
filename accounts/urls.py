from rest_framework.urls import path
from accounts.views import RegisterView, LoginView, login


app_name = 'accounts'
urlpatterns =[
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView, name="login"),
]

