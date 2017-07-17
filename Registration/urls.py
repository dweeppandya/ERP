from django.conf.urls import url

from . import views

urlpatterns = [
    # /register/student - Register Student
    url(r'^student/$', views.register, name='register'),

]
