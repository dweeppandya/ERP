# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from Registration.models import StudentDetails, Subject, Faculty


# Contains
# Division - Relation(Faculty,Subject) - Division
# StudentAttendance - Relation(Student,Subject) + attendance details
# Daily Attendance - date,time,attended(Derived from student attendance)


class Division(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    division = models.CharField(max_length=1)

    def __str__(self):
        return self.division + ' ' + self.faculty.first_name + ' ' + self.subject.subject_name


class StudentAttendance(models.Model):
    student = models.ForeignKey(StudentDetails, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    division = models.CharField(max_length=1)


class DailyAttendance(models.Model):
    date = models.DateField()
    time = models.TimeField()
    attended = models.BooleanField()
    student = models.ForeignKey(StudentAttendance)


class FacultyAttendance(models.Model):
    faculty = models.OneToOneField(Faculty)
    in_time = models.TimeField()
    out_time = models.TimeField()
