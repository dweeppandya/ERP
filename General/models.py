# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Faculty.models import Faculty


# Create your models here.

class Branch(models.Model):
    branch_name = models.CharField(max_length=10)
    HOD = models.OneToOneField(Faculty)


class Year(models.Model):
    branch = models.ForeignKey(Branch)
    year = models.CharField(max_length=2)


class Division(models.Model):
    division = models.CharField(max_length=2)
