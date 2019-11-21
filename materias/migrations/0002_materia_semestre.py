# Generated by Django 2.2.6 on 2019-11-13 22:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='semestre',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
