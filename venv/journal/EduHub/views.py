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
from django.shortcuts import render, get_object_or_404
from EduHub.forms import UserCreationForm, GradeForm



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

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    
    

  
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
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password1'))
            user.is_student = (role == 'student')
            user.is_teacher = (role == 'teacher')
            
            user.save()

            if role == 'teacher':
                teacher = Teacher.objects.create(
                    user=user,
                    firstname=form.cleaned_data.get('first_name'),
                    lastname=form.cleaned_data.get('last_name'),
                    username=username,
                    password=form.cleaned_data.get('password1'),
                    fullname=f"{form.cleaned_data.get('first_name') + ' ' + form.cleaned_data.get('last_name')}",
                    #courses=form.cleaned_data.get('course'),
                )
            elif role == 'student':
                student = Student.objects.create(
                    user=user,
                    firstname=form.cleaned_data.get('first_name'),
                    lastname=form.cleaned_data.get('last_name'),
                    username=username,
                    password=form.cleaned_data.get('password1'),
                    fullname=f"{form.cleaned_data.get('first_name') + ' ' + form.cleaned_data.get('last_name')}",
                    group=form.cleaned_data.get('group')
                )

            user = authenticate(username=username, password=form.cleaned_data.get('password1'))
            login(request, user)
            return redirect('home')

        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    
@login_required
def your_group(request):
    
    students = Student.objects.all()
    groups = Group.objects.all()
    template = loader.get_template('your_group.html')
    context = {
    'students': students,
    'groups': groups,
    
    
    }
    return HttpResponse(template.render(context, request))


def Your_Grade_Table(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    grades = Grade.objects.all()  
    context = {'students': students, 'courses': courses, 'grades': grades}
    return render(request, 'your_grade_table.html', context)

        
# def home(request):
#     user = request.user
#     try:
#         teacher = Teacher.objects.filter(user=user).first()
     
#         if teacher:
#             courses = Course.objects.filter(teacher=teacher)
#         else:
#             courses = Course.objects.none()  # Або встановіть якесь значення за замовчуванням
#         context = {'user': user, 'courses': courses, 'teacher': teacher}
#         return render(request, 'home.html', context)
#     except:
#         context = {'user': user}
#         return render(request, 'home.html', context)


def home(request):
    user = request.user
    context = {'user': user, 'search_attempted': False}
    try:
        teacher = Teacher.objects.filter(user=user).first()

        if teacher:
            courses = Course.objects.filter(teacher=teacher)
            context['courses'] = courses
            context['teacher'] = teacher

            if request.method == 'POST':
                search_lastname = request.POST.get('search_lastname')
                if search_lastname:
                    students = Student.objects.filter(lastname__icontains=search_lastname)
                    context['search_attempted'] = True

                    if students.count() == 1:
                        student = students.first()
                        return redirect('group_detail', course_id=student.group.course.course_id, group_id=student.group.group_id)
                    elif students.count() > 1:
                        context['students'] = students
                    else:
                        context['message'] = 'Студента з таким прізвищем не знайдено.'
        else:
            courses = Course.objects.none()
            context['courses'] = courses

    except Exception as e:
        print(f"Error in home view: {e}")

    return render(request, 'home.html', context)




def course_detail(request, course_id):
    course = get_object_or_404(Course, course_id=course_id)
    # Припустимо, що у вашій моделі Group є зв'язок з Course через ForeignKey.
    # Ви маєте використати правильне поле для фільтрації, тут в прикладі використовується 'course',
    # яке має вказувати на інстанс моделі Course.
    groups = Group.objects.filter(course=course)
    return render(request, 'course_detail.html', {'course': course, 'groups': groups})

def group_detail(request, course_id, group_id):
    course = get_object_or_404(Course, course_id=course_id)
    group = get_object_or_404(Group, group_id=group_id, course=course)
    students = Student.objects.filter(group=group)

    if request.method == 'POST':
        # Обробка форми
        for student in students:
            # Спроба знайти існуючий об'єкт Grade або створити новий
            grade, created = Grade.objects.get_or_create(
                student=student, 
                course=course,
                defaults={'module1': 0, 'module2': 0, 'module3': 0, 'module4': 0, 'grade': 0}
            )
            form = GradeForm(request.POST, instance=grade, prefix=str(student.stud_id))
            if form.is_valid():
                form.save()
        return redirect('group_detail', course_id=course_id, group_id=group_id)
    else:
        # Ініціалізація форм для кожного студента
        grade_forms = {}
        
        for student in students:
            grade, created = Grade.objects.get_or_create(
                student=student, 
                course=course,
                defaults={'module1': 0, 'module2': 0, 'module3': 0, 'module4': 0, 'grade': 0}
            )
            grade_forms[student.stud_id] = GradeForm(instance=grade, prefix=str(student.stud_id))

        #return render(request, 'group_detail.html', {'group': group, 'students': students, 'grade_forms': grade_forms})
        return render(request, 'group_detail.html', {'group': group, 'students': students, 'grade_forms': grade_forms})
   
