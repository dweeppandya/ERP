from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    # url(r'^', include('Faculty.urls')),
    url(r'^admin/', admin.site.urls),
]
