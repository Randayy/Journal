from django.http import HttpResponse
from django.template import loader
from .models import Student, Teacher
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect

from EduHub.forms import CustomUserCreationForm


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
        context = {'form': CustomUserCreationForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            role = form.cleaned_data.get('role')  # Отримання вибраної ролі з форми

            if role == 'teacher':
                # Створення запису вчителя
                Teacher.objects.create(
                    firstname="Не задано",
                    lastname="Не задано",
                    fullname=f"{user.first_name} {user.last_name}",
                    username=username,
                    password=form.cleaned_data.get('password1'),  # Зауважте: у реальних системах пароль необхідно зберігати у безпечному вигляді
                    subject="Не вказано",  # Вам потрібно буде додати логіку для обробки цих даних
                    department="Не вказано"
                )
            elif role == 'student':
                # Створення запису студента
                Student.objects.create(
                    firstname="Не задано",
                    lastname="Не задано",
                    fullname=f"{user.first_name} {user.last_name}",
                    username=username,
                    password=form.cleaned_data.get('password1'),  # Аналогічно, зберігайте паролі безпечно
                    group="Не вказано"
                )

            # # Автентифікація та логін користувача
            # user = authenticate(username=username, password=form.cleaned_data.get('password1'))
            # if user is not None:
            #     login(request, user)
            #     return redirect('home')  # Перенаправлення на головну сторінку або іншу цільову сторінку

        return render(request, self.template_name, {'form': form})