import json

from django.http import JsonResponse
from django.shortcuts import render

from course.models import course

# Create your views here.


def index(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        body = {**{"id": len(course) + 1}, **body}
        course.append(body)
    return JsonResponse(course, safe=False)


def course_id(request, course_id):
    if request.method == 'PUT':
        for x in range(len(course)):
            if course[x]["id"] == course_id:
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                course[x] = {**body, **{"id": course_id}}
                break
        return JsonResponse(course, safe=False)
    courseTmp = {}
    for x in course:
        if x["id"] == course_id:
            courseTmp = x
            break
    return JsonResponse(courseTmp, safe=False)


def edit(request, course_id):
    if request.method == 'PUT':
        for x in course:
            if x["id"] == course_id:
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                x = {**body, **{"id": course_id}}
                break
    return JsonResponse(course, safe=False)
