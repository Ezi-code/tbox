from django.db import models
from django.db.models.query import QuerySet
# from contacts.models import Subcontractor
import typing 

if typing.TYPE_CHECKING:
    from contacts.models import Subcontractor

class ProjectManager(models.Manager):
    # from contacts.models import Subcontractor

    def get_queryset(self) -> QuerySet['Subcontractor']:
        subcontractor = Subcontractor.objects.all()

        return super().get_queryset()

# Create your models here.
class Project(models.Model):
    subcontractor: QuerySet[Subcontractor] = ProjectManager()

    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    # subcontractor = models.ManyToManyField(Contract, blank=True)


    def __str__(self):
        return self.title