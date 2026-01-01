from django.contrib import admin

# Register your models here.
from employees.models import CustomUser

admin.site.register(CustomUser)
