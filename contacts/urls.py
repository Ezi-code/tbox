from rest_framework.urls import path
from .views import ContractList, ContractDetail,SubcontractorList

app_name = 'contacts'

urlpatterns = [
    path('', ContractList.as_view()),
    path('<int:pk>/', ContractDetail.as_view()),
    path('subcontractor/', SubcontractorList.as_view()),

]