from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import include, path
from EduHub.views import Register

urlpatterns = [
    # path('EduHub/', views.EduHub, name='EduHub'),
    path('about/', views.EduHub_loginned, name='about'),
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('your_group/', views.your_group, name='your_group'),
    path('grade_table/', views.grade_table, name='grade_table'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('your_grade_table/', views.Your_Grade_Table, name='your_grade_table'),
    path("home", views.home, name="home"),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('courses/<int:course_id>/groups/<int:group_id>/', views.group_detail, name='group_detail'),

]

