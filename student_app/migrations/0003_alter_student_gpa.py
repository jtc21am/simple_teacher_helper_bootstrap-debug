# Generated by Django 3.2.16 on 2022-12-18 21:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0002_auto_20221218_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gpa',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]