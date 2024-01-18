from django.db import models
from project.models import Project


# Create your models here.
class Contract(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
    


class Subcontractor(models.model):

    def __init__(self, arg):
        super(Subcontractor, self).__init__()
        self.arg = arg
        
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)