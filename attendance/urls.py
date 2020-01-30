from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/<int:course_id>/<str:student_id>', views.attendance, name="attendance")
]
