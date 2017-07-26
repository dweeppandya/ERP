from django.db import models

class Student(models.Model):
    gr_number = models.CharField(max_length=10)


