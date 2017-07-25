# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from Registration.models import StudentDetails


# Create your views here.
def index(request):
    all_students = StudentDetails.objects.all()
    return render(request, "attendance.html", {
        'all_students': all_students
    })
