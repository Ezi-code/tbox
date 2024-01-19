from django.db import models
from project.models import Project
from project.models import Project

# Create your models here.
class Contract(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.PROTECT, default=1)
    sub_contractor = models.ForeignKey('Subcontractor', on_delete=models.CASCADE, default=1, related_name='contracts')

    def __str__(self):
        return self.name
    


class Subcontractor(models.Model):        
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    contract = models.ManyToManyField(Contract)
    project = models.ManyToManyField(Project)

    def __str__(self):
        return self.name