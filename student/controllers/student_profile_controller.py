from rest_framework.response import Response
from rest_framework.decorators import api_view
from utils.factory.student_factory import StudentFactory


@api_view()
def get_student_by_roll(request, rollno):
    return Response({'msg': rollno})

@api_view(['POST'])
def get_student(request):
    print(request.POST)

@api_view(['POST'])
def add_student(request):
    return Response({hello})

@api_view(['POST'])
def ban_student(request):
    return Response({hello})

@api_view(['DELETE'])
def delete_student(request):
    pass
