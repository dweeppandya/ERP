# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Faculty.models import *


# Create your models here.

class Branch(models.Model):
    branch_name = models.CharField(max_length=10)
    HOD = models.OneToOneField(Faculty)


class Year(models.Model):
    branch = models.ForeignKey(Branch)
    year = models.CharField(max_length=2)


class Subject(models.Model):
    subject_code = models.IntegerField(primary_key=True)
    subject_name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty)
    divsion = models.ForeignKey(Division)
    year = models.ForeignKey(Year)


class Division(models.Model):
    division = models.CharField(max_length=2)
