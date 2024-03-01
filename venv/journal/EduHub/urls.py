from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('EduHub/', views.EduHub, name='EduHub'),
    path('EduHub/success', views.EduHub_loginned, name='EduHub_loginned'),
    path('accounts/login/', views.login_view, name='login'),
    # path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout')
]