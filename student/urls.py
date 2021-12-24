from django.urls import path, include
from student.controllers.student_profile_controller import *

urlpatterns = [
    path('roll/<rollno>/', get_student_by_roll, 
    name="get_student_by_rollno"),

    path('', get_student, name="get_student"),

    path('add/', add_student, name="add_student"),

    path('ban/', ban_student, name="ban_student"),

    path('delete/', delete_student, name="delete student")
]