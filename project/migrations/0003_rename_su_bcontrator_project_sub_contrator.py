# Generated by Django 3.2.23 on 2024-01-18 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_su_bcontrator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='su_bcontrator',
            new_name='sub_contrator',
        ),
    ]
