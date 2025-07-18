from django.urls import path
from . import views 
from .views import student_home, student_edit, student_delete
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.student_home, name='student-home'),
    path('students/', views.student_list),
    path('students/<int:pk>/', views.student_detail),

    path('', student_home, name='student-home'),
    path('edit/<int:pk>/', student_edit, name='student-edit'),
    path('delete/<int:pk>/', student_delete, name='student-delete'),

     path('login/', LoginView.as_view(template_name='students/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
