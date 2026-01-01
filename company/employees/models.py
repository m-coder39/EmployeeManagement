# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Employee(models.Model):
    empid = models.IntegerField()
    name = models.CharField(max_length=20)
    deptname = models.CharField(max_length=20)
    salary = models.IntegerField()
    designation = models.CharField(max_length=20)
    image = models.ImageField(upload_to='employees')


class CustomUser(AbstractUser):
    empid = models.IntegerField()
    name = models.CharField(max_length=11)
    deptname = models.CharField(max_length=20)
    salary = models.IntegerField()
    designation = models.CharField(max_length=20)
    image = models.ImageField(upload_to='employees')

    def save(self, *args, **kwargs):
        if self.is_superuser:
            if not self.empid:
                self.empid = 0
            if not self.name:
                self.name = 'Admin'
            if not self.deptname:
                self.deptname = 'AdminDept'
            if not self.salary:
                self.salary = 0
            if not self.designation:
                self.designation = 'Admin'
            if not self.image:
                self.image = 'default.png'
        super().save(*args, **kwargs)
