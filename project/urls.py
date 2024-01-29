from rest_framework.urls import path
from .views import ProjectList, ProjectDetail, ProjectSubcontractorView, SeacrProjectView


app_name = "project"
urlpatterns = [
    path("", ProjectList.as_view(), name="project-list"),
    path("<str:search>", SeacrProjectView.as_view(), name="search"),
    path("<int:pk>/", ProjectDetail.as_view(), name="project-detail"),
    path(
        "<int:pk>/subcontractor/",
        ProjectSubcontractorView.as_view(),
        name="project-subcontractor",
    ),
]
