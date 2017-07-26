# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import StudentForm, FacultyForm, SubjectForm


def register_student(request):
    if request.method == "POST":
        print("Register student post")
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            print("Valid")
            form.save()
            return HttpResponseRedirect('/register/student/')
            # return HttpResponse(form.errors)
        else:
            print(form.errors)
            # return HttpResponse(form.errors)
        return render(request, "register_student.html", {'form': form})
    else:
        print("Register student not POST")
        form = StudentForm()
        return render(request, "register_student.html", {'form': form})


def register_faculty(request):
    if request.method == "POST":
        print("Register faculty post")
        form = FacultyForm(request.POST, request.FILES)
        if form.is_valid():
            print("Valid")
            form.save()
            return HttpResponseRedirect('/register/faculty/')
            # return HttpResponse(form.errors)
        else:
            print(form.errors)
            # return HttpResponse(form.errors)
        return render(request, "register_faculty.html", {'form': form})
    else:
        print("Register faculty not POST")
        form = FacultyForm()

    return render(request, "register_faculty.html", {'form': form})


def register_subject(request):
    if request.method == "POST":
        print("Register subject post")
        form = SubjectForm(request.POST, request.FILES)
        if form.is_valid():
            print("Valid")
            form.save()
            return HttpResponseRedirect('/register/subject/')
            # return HttpResponse(form.errors)
        else:
            print(form.errors)
            # return HttpResponse(form.errors)
        return render(request, "register_subject.html", {'form': form})
    else:
        print("Register subject not POST")
        form = SubjectForm()

    return render(request, "register_subject.html", {'form': form})