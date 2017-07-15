# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from Faculty.models import *


# Create your models here.

class Branch(models.Model):
    branch_name = models.CharField(max_length=10)
    HOD = models.OneToOneField(Faculty, on_delete=models.CASCADE)


class Year(models.Model):
    branch = models.ForeignKey(Branch,  on_delete=models.CASCADE)
    year = models.CharField(max_length=2)


class Division(models.Model):
    division = models.CharField(max_length=2)


class Subject(models.Model):
    subject_code = models.IntegerField(primary_key=True)
    subject_name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    divsion = models.ForeignKey(Division, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
