from django.db import models
from django.core.validators import MinLengthValidator
from django.db import models




class Student(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  fullname = models.CharField(max_length=255)
  username = models.CharField(max_length=255)
  password = models.CharField(validators=[
            MinLengthValidator(6, 'the field must contain at least 6 characters')
            ],max_length=50)
  group = models.CharField(max_length=10)
  stud_id = models.IntegerField()

