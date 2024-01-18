from django.contrib import admin
from .models import Contract, Subcontractor
# Register your models here.
admin.site.register([Contract, Subcontractor])