from django.http import JsonResponse
from django.shortcuts import render
from course.models import course

# Create your views here.


def index(request):
    return JsonResponse(course, safe=False)


def attendance(request, course_id, student_id):
    courseTmp = {}
    for x in course:
        if x["id"] == course_id:
            courseTmp = x
            break
    for x in courseTmp["student"]:
        if x["id"] == student_id:
            x["check"] = True
            break
    return JsonResponse(courseTmp, safe=False)
