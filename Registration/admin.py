# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Subject, StudentDetails, Faculty

# Register your models here.
admin.site.register(StudentDetails)
admin.site.register(Subject)
admin.site.register(Faculty)
