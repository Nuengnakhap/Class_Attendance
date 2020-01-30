import json

from django.http import JsonResponse
from django.shortcuts import render

from student.models import student

# Create your views here.


def index(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        student.append(body)
    return JsonResponse(student, safe=False)


def edit(request, student_id):
    if request.method == 'PUT':
        for x in student:
            if x["id"] == student_id:
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                x["name"] = body["name"]
                break
    return JsonResponse(student, safe=False)
