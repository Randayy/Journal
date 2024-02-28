from django.http import HttpResponse
from django.template import loader
from .models import Student
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def EduHub(request):
  # students = Student.objects.all().values()
  template = loader.get_template('index.html')
  # context = {
  #   'students': students,
  # }
  return HttpResponse(template.render({}, request))

# @login_required
def EduHub_loginned(request):
  students = Student.objects.all().values()
  template = loader.get_template('index_logined.html')
  context = {
    'students': students,
  }
  return HttpResponse(template.render(context, request))


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

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            student = Student.objects.get(username=username, password=password)
            return redirect('EduHub_loginned')
        except Student.DoesNotExist:
            return redirect('EduHub')
    return render(request, 'login.html')

