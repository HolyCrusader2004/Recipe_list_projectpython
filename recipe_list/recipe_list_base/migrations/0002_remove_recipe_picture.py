# Generated by Django 5.0.1 on 2024-01-25 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_list_base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='picture',
        ),
    ]
