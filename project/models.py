from django.db import models
from django.db.models.query import QuerySet
from contacts.models import Subcontractor


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    subcontrator = models.ForeignKey(Subcontractor, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title