# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .forms import StudentForm


# Create your views here.
def register(request):
    form = StudentForm()

    return render(request, "register.html", {'form': form})
