from rest_framework.urls import path
from .views import ProjectList, ProjectDetail   


app_name = 'project'
urlpatterns = [
    path('', ProjectList.as_view()),
    path('<int:pk>/', ProjectDetail.as_view()),

]
