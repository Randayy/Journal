from django.contrib import admin

from django.contrib import admin
from .models import Teacher, Student, Course, Enrollment, Grade, user

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()
#це все для відображення первинного ключа
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'firstname', 'lastname')

class StudentAdmin(admin.ModelAdmin):

    list_display = ('stud_id', 'firstname', 'lastname','username', 'password')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_name', 'teacher')

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('enrollmer_id', 'student', 'course')

class GradeAdmin(admin.ModelAdmin):
    list_display = ('grade_id', 'student', 'course', 'grade', 'date')
    
# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    pass


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Grade, GradeAdmin)