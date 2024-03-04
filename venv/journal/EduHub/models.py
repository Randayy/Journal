from django.db import models
from django.contrib import admin
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  is_student = models.BooleanField(default=False)
  is_teacher = models.BooleanField(default=False)
  
class Course(models.Model):
  course_id = models.AutoField(primary_key=True)
  course_name = models.CharField(max_length=255)
  # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, db_column='teacher_id')
  def __str__(self):
      return self.course_name
class Group(models.Model):
  group_id = models.AutoField(primary_key=True)
  group_name = models.CharField(max_length=255)
  # students = models.OneToManyField(Student, related_name='group')
  
  def __str__(self):
    return self.group_name
  
class Teacher(models.Model):
  teacher_id = models.AutoField(primary_key=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
  is_teacher = models.BooleanField(default=True)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  fullname = models.CharField(max_length=255)
  username = models.CharField(max_length=255)
  password = models.CharField(validators=[
            MinLengthValidator(6, 'the field must contain at least 6 characters')
            ],max_length=50,default="123456")
  subject = models.CharField(max_length=255)
  department = models.CharField(max_length=255)
  courses = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='teacher', null=True)
  def __str__(self):
      return f"{self.fullname} - {self.subject}"

class Student(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
  is_student = models.BooleanField(default=True)
  stud_id = models.AutoField(primary_key=True)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  fullname = models.CharField(max_length=255)
  username = models.CharField(max_length=255)
  password = models.CharField(validators=[
            MinLengthValidator(6, 'the field must contain at least 6 characters')
            ],max_length=50,default="123456")
  group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students', null=True)
  # enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name='student', null=True)

  def __str__(self):
      return self.fullname
    
  def get(self):
    return f"{self.username} - {self.group.group_name}"

class Enrollment(models.Model):
  enrollment_id = models.AutoField(primary_key=True)
  student = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='student_id')
  course = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='course_id')
  
  def __str__(self):
    return f"{self.student.fullname} - {self.course.course_name}"
  
class Grade(models.Model):
  grade_id = models.AutoField(primary_key=True)
  student = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='student_id')
  # course = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='course_id')
  enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, db_column='enrollment_id',blank=True, null=True)
  grade = models.IntegerField()
  date = models.DateField()

  def __str__(self):
    return f"{self.student.fullname} - {self.enrollment.course}: {self.grade}"
  

