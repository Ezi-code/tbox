# Generated by Django 3.2.23 on 2024-01-19 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contract_sub_contractor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcontractor',
            name='contract',
        ),
        migrations.AddField(
            model_name='subcontractor',
            name='contract',
            field=models.ManyToManyField(to='contacts.Contract'),
        ),
    ]