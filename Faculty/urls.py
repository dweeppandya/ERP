from django.conf.urls import url
from . import views

urlpatterns = [
    #For testing
    url(r'$', views.test, name='test'),

]
