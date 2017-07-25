# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from Registration.models import StudentDetails


# Create your views here.
def index(request):
    all_students = StudentDetails.objects.all()
    return render(request, "attendance.html", {
        'all_students': all_students
    })


def save(request):
    if request.method == 'POST':
        print("Saving customers")
        all_students = StudentDetails.objects.all().values_list('id')
        for i in request.POST:
            print(i)
    else:
        print("Not here because of post")
    return HttpResponse("Here")