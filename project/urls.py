from rest_framework.urls import path
from .views import ProjectList, ProjectDetail, ProjectSubcontractorView   


app_name = 'project'
urlpatterns = [
    path('', ProjectList.as_view(), name='project-list'),
    path('<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
    path('<int:pk>/subcontractor/', ProjectSubcontractorView.as_view(), name='project-subcontractor'),

]
