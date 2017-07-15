from django.db import models

# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # "user_%d" % instance.owner.id, "car_%s" % instance.slug, filename
    return 'user_{0}/{1}'.format(instance.gr_number, filename)


class StudentDetails(models.Model):
    # Basic Details
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    DOB = models.DateField(default='1996-02-11')
    admission_type = models.CharField(max_length=50)
    shift = models.CharField(max_length=1)
    caste_type = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)
    gr_number = models.AutoField(primary_key=True)

    # personal details
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField(default=0)
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
    father_mobile = models.BigIntegerField(default=0)
    father_email = models.EmailField()
    # mother
    mother_name = models.CharField(max_length=50)
    mother_profession = models.CharField(max_length=30)
    mother_designation = models.CharField(max_length=30)
    mother_mobile = models.BigIntegerField(default=0)
    mother_email = models.EmailField(null=True)

    # permanent address
    permanent_address = models.CharField(max_length=100)
    permanent_state = models.CharField(max_length=50)
    permanent_city = models.CharField(max_length=50)
    permanent_pin_code = models.DecimalField(default=000)
    permanent_country = models.CharField(max_length=50)

    # current address
    current_address = models.CharField(max_length=100)
    current_state = models.CharField(max_length=50)
    current_city = models.CharField(max_length=50)
    current_pin_code = models.IntegerField()
    current_country = models.CharField(max_length=50)

    # Exam details
    jee_physics = models.PositiveIntegerField(default=0)
    jee_maths = models.PositiveIntegerField(default=0)
    jee_chemistry = models.PositiveIntegerField(default=0)
    jee_total = models.PositiveIntegerField(default=0)
    jee_max_physics = models.PositiveIntegerField(default=0)
    jee_max_maths = models.PositiveIntegerField(default=0)
    jee_max_chemistry = models.PositiveIntegerField(default=0)

    # documents
    doc_tenth_marksheet = models.FileField(upload_to=user_directory_path)
    doc_twelfth_marksheet = models.FileField(upload_to=user_directory_path)
    doc_jee_marksheet = models.FileField(upload_to=user_directory_path)
    doc_profile_pic = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        return self.first_name + ' ' + str(self.pk)



class Faculty(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    DOB = models.DateField(default='1996-02-11')


    #account details
    salary = models.IntegerField(default=10)


    #teaching
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
    father_mobile = models.BigIntegerField(blank= True)
    father_email = models.EmailField(blank= True)
    # mother
    mother_name = models.CharField(max_length=50)
    mother_profession = models.CharField(max_length=30)
    mother_designation = models.CharField(max_length=30)
    mother_mobile = models.BigIntegerField()
    mother_email = models.EmailField(null=True, blank= True)

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








class StudentMaster(models.Model):
    student = models.OneToOneField(StudentDetails)


class Branch(models.Model):
    branch_name = models.CharField(max_length=10)
    HOD = models.OneToOneField()


class Year(models.Model):
    branch = models.ForeignKey(Branch)
    year = models.CharField(max_length=2)


class Attendance(models.Model):
