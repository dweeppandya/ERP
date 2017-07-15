# Register your models here.

from django.contrib import admin

from .models import Branch,Year,Division

admin.site.register(Branch)
admin.site.register(Year)
admin.site.register(Division)
