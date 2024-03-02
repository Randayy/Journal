from django.http import HttpResponse
from django.template import loader
from .models import Student
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect

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
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)