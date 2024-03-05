from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import include, path
from EduHub.views import Register

urlpatterns = [
    path('EduHub/', views.EduHub, name='EduHub'),
    path('about/', views.EduHub_loginned, name='about'),
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('your_group/', views.your_group, name='your_group'),
    path('grade_table/', views.grade_table, name='grade_table'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout')
]