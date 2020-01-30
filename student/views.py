from django.http import JsonResponse
from django.shortcuts import render
from student.models import student
# Create your views here.


def index(request):
    if request.method == 'POST':
        student.append(request.body)
    return JsonResponse(student, safe=False)
