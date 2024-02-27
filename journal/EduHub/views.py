from django.http import HttpResponse
from django.template import loader
from .models import Student

def EduHub(request):
  students = Student.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'students': students,
  }
  return HttpResponse(template.render(context, request))