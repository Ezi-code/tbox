# Generated by Django 3.2.23 on 2024-02-01 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountholder',
            old_name='user_id',
            new_name='id',
        ),
    ]
