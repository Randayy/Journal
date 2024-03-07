from django.db import models
from django.contrib import admin
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class User(AbstractUser):
  is_student = models.BooleanField(default=False)
  is_teacher = models.BooleanField(default=False)
  
  
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
  # subject = models.CharField(max_length=255)
  # department = models.CharField(max_length=255)
  # courses = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='teacher', null=True)
  def __str__(self):
      return f"{self.fullname}"
class Course(models.Model):
  course_id = models.AutoField(primary_key=True)
  course_name = models.CharField(max_length=255)
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, db_column='teacher_id')
  def __str__(self):
      return self.course_name
class Group(models.Model):
  group_id = models.AutoField(primary_key=True)
  group_name = models.CharField(max_length=255)
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.group_name

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
  group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
  # grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='student_grades')
  def __str__(self):
      return self.fullname
    
  def get(self):
    return f"{self.username} - {self.group.group_name}"

  
class Grade(models.Model):
  grade_id = models.AutoField(primary_key=True)
  student = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='student_id')
  course = models.ForeignKey(Course, on_delete=models.CASCADE, db_column='course_id')
  grade = models.DecimalField(max_digits=5, decimal_places=2)
  module1 = models.IntegerField()
  module2 = models.IntegerField()
  module3 = models.IntegerField()
  module4 = models.IntegerField()

  def __str__(self):
    return f'{self.grade}'
  
  
# class CustomUser(AbstractUser):
#     is_student = models.BooleanField(default=False)
#     is_teacher = models.BooleanField(default=False)

# class Teacher(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

# class Course(models.Model):
#     name = models.CharField(max_length=100)
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

# class Group(models.Model):
#     name = models.CharField(max_length=100)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)

# class Student(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)

# class Grade(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     grade = models.DecimalField(max_digits=5, decimal_places=2)


