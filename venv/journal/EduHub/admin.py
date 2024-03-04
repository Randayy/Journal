from django.contrib import admin

from django.contrib import admin
from .models import Teacher, Student, Course, Enrollment, Grade, User, Group

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()
#це все для відображення первинного ключа
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'firstname', 'lastname','username', 'password')

class StudentAdmin(admin.ModelAdmin):

    list_display = ('stud_id', 'firstname', 'lastname','username', 'password','group')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_name')

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('enrollment_id', 'student', 'course')

class GradeAdmin(admin.ModelAdmin):
    list_display = ('grade_id', 'student', 'grade', 'date','enrollment')
    
# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_student', 'is_teacher', 'is_staff', 'is_active')

class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_id', 'group_name')
    
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Group, GroupAdmin)