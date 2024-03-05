from django.http import HttpResponse
from django.template import loader
from EduHub.models import Student
from EduHub.models import Teacher
from EduHub.models import User
from EduHub.models import Group
from EduHub.models import Course
from EduHub.models import Grade
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect
# from django.forms.BaseForm import clean_data
from .models import *

from EduHub.forms import UserCreationForm


def EduHub(request):
  # students = Student.objects.all().values()
  template = loader.get_template('index.html')
  # context = {
  #   'students': students,
  # }
  return HttpResponse(template.render({}, request))

# @login_required
def EduHub_loginned(request):
  students = Student.objects.all()
  groups = Group.objects.all()
  needed_name = 'КН-31'
  template = loader.get_template('index_logined.html')
  context = {
    'students': students,
    'groups': groups,
    
  }
  return HttpResponse(template.render(context, request))

def grade_table(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    grades = Grade.objects.all()  
    context = {'students': students, 'courses': courses, 'grades': grades}
    return render(request, 'grade_table.html', context)

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None and user.is_authenticated:
#             login(request, user)
#             return render(request, 'index_logined.html')
#         else:
#             return render(request, 'not_succes_login.html')
#     else:
#         return render(request, 'logged_out.html')

# def logout_view(request):
#     logout(request)
#     # Redirect to a success page.
    
    
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         try:
#             student = Student.objects.get(username=username, password=password)
#             return redirect('EduHub_loginned')
#         except Student.DoesNotExist:
#             return redirect('EduHub')
#     return render(request, 'login.html')
  
class Register(View):
    template_name = 'registration/register.html'
    

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            role = form.cleaned_data.get('role')

            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password1'))
            user.is_student = (role == 'student')
            user.is_teacher = (role == 'teacher')
            
            user.save()

            if role == 'teacher':
                teacher = Teacher.objects.create(
                    user=user,
                    firstname="Не задано",
                    lastname="Не задано",
                    username=username,
                    password=form.cleaned_data.get('password1'),
                    fullname="Не задано",
                    subject="Не вказано",
                    department="Не вказано",
                    courses=form.cleaned_data.get('course'),
                )
            elif role == 'student':
                student = Student.objects.create(
                    user=user,
                    firstname="Не задано",
                    lastname="Не задано",
                    username=username,
                    password=form.cleaned_data.get('password1'),
                    fullname="Не задано",
                    group=form.cleaned_data.get('group')
                )

            user = authenticate(username=username, password=form.cleaned_data.get('password1'))
            login(request, user)
            return redirect('home')

        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    

def your_group(request):
    
    students = Student.objects.all()
    groups = Group.objects.all()
    studentskn31 = Student.objects.filter(group__group_name='КН-31').values()
    template = loader.get_template('your_group.html')
    context = {
    'students': students,
    'groups': groups,
    
    
    }
    return HttpResponse(template.render(context, request))

        