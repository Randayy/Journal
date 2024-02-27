from django.urls import path
from . import views

urlpatterns = [
    path('EduHub/', views.EduHub, name='EduHub'),
]