from django.db import models
from General.models import Student
from Registration.models import Subject


class Enrollment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Online(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    marks = models.IntegerField()
    max_marks = models.IntegerField()


class Theory(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    marks = models.IntegerField()
    max_marks = models.IntegerField()


class TermWork:
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    marks = models.IntegerField()
    max_marks = models.IntegerField()


class Practical:
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    marks = models.IntegerField()
    max_marks = models.IntegerField()
