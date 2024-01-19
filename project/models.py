from django.db import models
from django.apps import apps



# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    sub_contractor = models.ManyToManyField('contacts.Subcontractor', related_name='projects')

    def __str__(self):
        return self.title