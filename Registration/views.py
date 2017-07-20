# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .forms import StudentForm, FacultyForm, SubjectForm


def register_student(request):
    form = StudentForm()

    return render(request, "register_student.html", {'form': form})


def register_faculty(request):
    form = FacultyForm()

    return render(request, "register_faculty.html", {'form': form})


def register_subject(request):
    form = SubjectForm()

    return render(request, "register_subject.html", {'form': form})
