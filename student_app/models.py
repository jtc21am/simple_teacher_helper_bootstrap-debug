from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator



# Create your models here.




class Student(models.Model):
  studentnumber = models.PositiveIntegerField()
  firstname = models.CharField(max_length=50)
  lastname = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  telephone = models.CharField(max_length=50)
  fieldofstudy = models.CharField(max_length=50)
  gpa = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5.0)])

  
