from django.shortcuts import render

from django.http import JsonResponse

from rest_framework.viewsets import ModelViewSet

from .models import Student
from .serializers import StudentSerializer

# Create your views here.


class StudentsViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

