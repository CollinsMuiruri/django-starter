from django.shortcuts import render
from .models import *
from shule_users.models import *

def index(request):
    teacher = Teacher.objects.all()
    student = Student.objects.all()
    parent = ParentOrGuardian.objects.all()
    context = {
        "teacher": teacher,
        "student": student,
        "parent": parent,
    }
    return render(request, "shule_app/index.html", context)
