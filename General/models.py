# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Branch(models.Model):
    branch_name = models.CharField(max_length=10)
    HOD = models.OneToOneField()


class Year(models.Model):
    branch = models.ForeignKey(Branch)
    year = models.CharField(max_length=2)


class Subject(models.Model):
    subject_code = models.IntegerField(primary_key=True)
    subject_name = models.CharField(max_length=100)

