from django.db import models
from django.contrib import admin
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class user(AbstractUser):
  pass

class Teacher(models.Model):
  teacher_id = models.AutoField(primary_key=True)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  fullname = models.CharField(max_length=255)
  username = models.CharField(max_length=255)
  password = models.CharField(validators=[
            MinLengthValidator(6, 'the field must contain at least 6 characters')
            ],max_length=50)
  subject = models.CharField(max_length=255)
  department = models.CharField(max_length=255)
  def __str__(self):
      return f"{self.fullname} - {self.subject}"

class Student(models.Model):
  stud_id = models.AutoField(primary_key=True)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  fullname = models.CharField(max_length=255)
  username = models.CharField(max_length=255)
  password = models.CharField(validators=[
            MinLengthValidator(6, 'the field must contain at least 6 characters')
            ],max_length=50)
  group = models.CharField(max_length=10)

  def __str__(self):
      return self.fullname

  

class Course(models.Model):
  course_id = models.AutoField(primary_key=True)
  course_name = models.CharField(max_length=255)
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, db_column='teacher_id')
  def __str__(self):
      return self.course_name


class Enrollment(models.Model):
  enrollmer_id = models.AutoField(primary_key=True)
  student = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='student_id')
  course = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='course_id')

class Grade(models.Model):
  grade_id = models.AutoField(primary_key=True)
  student = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='student_id')
  course = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='course_id')
  grade = models.IntegerField(max_length = 3)
  date = models.DateField()

