# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Division, DailyAttendance, StudentAttendance

# Register your models here.

admin.site.register(Division)
admin.site.register(DailyAttendance)
admin.site.register(StudentAttendance)
