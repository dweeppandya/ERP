# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import StudentDetails, StudentMaster

# Register your models here.
admin.site.register(StudentMaster)
admin.site.register(StudentDetails)
