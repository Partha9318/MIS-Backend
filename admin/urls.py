from django.urls import path

from admin.controllers.student_notification_controller import *

urlpatterns = [

    path('student/notify/', notify_by_batch, 
    name="student_notifier"),

    path('student/add/subscription', add_student_subscription,
    name="add_student_subscription"),

    path('student/remove/subscription', remove_student_subscription,
    name="remove_student_subscription"),

    path('student/veirfy', verify_student,
    name="verify_student")
    
]
