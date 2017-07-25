from django.conf.urls import url

from . import views

app_name = 'registration'

urlpatterns = [
    # /register/student - Register Student
    url(r'^student/$', views.register_student, name='register_student'),
    # /register/faculty - Register Faculty
    url(r'^faculty/$', views.register_faculty, name='register_faculty'),
    # /register/subject - Register Subject
    url(r'^subject/$', views.register_subject, name='register_subject'),

]
