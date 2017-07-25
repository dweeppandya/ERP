# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render, HttpResponse

from .forms import StudentForm, FacultyForm, SubjectForm


def register_student(request):
    if request.method == "POST":
        print("POST")
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            print("Valid")
            form.save()
            return HttpResponse(form.errors)
        else:
            print(form.errors)
            return HttpResponse(form.errors)
    else:
        print("not POST")
        form = StudentForm()
        return render(request, "register_student.html", {'form': form})


def register_faculty(request):
    form = FacultyForm()

    return render(request, "register_faculty.html", {'form': form})


def register_subject(request):
    form = SubjectForm()

    return render(request, "register_subject.html", {'form': form})
