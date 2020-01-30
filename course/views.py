from django.http import JsonResponse
from django.shortcuts import render

from course.models import course

# Create your views here.


def index(request):
    return JsonResponse(course, safe=False)


def course_id(request, course_id):
    courseTmp = {}
    for x in course:
        if x["id"] == course_id:
            courseTmp = x
            break
    return JsonResponse(courseTmp, safe=False)
