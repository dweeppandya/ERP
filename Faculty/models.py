from django.db import models


# Create your models here.

def user_directory_path(instance, filename):
    return 'Faculty/{0}/{1}/{2}'.format(instance.branch, instance.faculty_code, filename)


class Faculty(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    DOB = models.DateField(default='1996-02-11')

    faculty_code = models.CharField(max_length=50)

    # account details
    salary = models.IntegerField(default=10)

    # teaching
    teaching_experience = models.PositiveIntegerField(default=0)
    subjects_experience = models.CharField(max_length=250)
    projects = models.TextField(max_length=300)

    # personal details
    caste_type = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField(default="0")
    religion = models.CharField(max_length=20)
    sub_caste = models.CharField(max_length=30)
    handicapped = models.BooleanField(default=0)
    nationality = models.CharField(max_length=50)

    # emergency contact
    emergency_name = models.CharField(max_length=50)
    emergency_mobile = models.BigIntegerField()
    emergency_relation = models.CharField(max_length=50)
    emergency_address = models.CharField(max_length=100)

    # family
    # father
    father_name = models.CharField(max_length=50)
    father_profession = models.CharField(max_length=30)
    father_designation = models.CharField(max_length=30)
    father_mobile = models.BigIntegerField(blank=True)
    father_email = models.EmailField(blank=True)
    # mother
    mother_name = models.CharField(max_length=50)
    mother_profession = models.CharField(max_length=30)
    mother_designation = models.CharField(max_length=30)
    mother_mobile = models.BigIntegerField()
    mother_email = models.EmailField(null=True, blank=True)

    # permanent address
    permanent_address = models.CharField(max_length=100)
    permanent_state = models.CharField(max_length=50)
    permanent_city = models.CharField(max_length=50)
    permanent_pin_code = models.IntegerField()
    permanent_country = models.CharField(max_length=50)

    # current address
    current_address = models.CharField(max_length=100)
    current_state = models.CharField(max_length=50)
    current_city = models.CharField(max_length=50)
    current_pin_code = models.IntegerField()
    current_country = models.CharField(max_length=50)

    # documents

    doc = models.FileField(upload_to=user_directory_path)
    doc_profile_pic = models.FileField(upload_to=user_directory_path)

