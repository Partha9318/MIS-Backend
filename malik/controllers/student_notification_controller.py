from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def notify_by_batch(request):
    pass

@api_view(['POST'])
def add_student_subscription(request):
    pass

@api_view(['POST'])
def remove_student_subscription(request):
    pass

@api_view(['POST'])
def verify_student(request):
    pass