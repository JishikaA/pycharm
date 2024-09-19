from tkinter.constants import CASCADE

from django.db import models

# Create your models here.
class Test(models.Model):
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=50)
    date=models.DateField()


class Department(models.Model):
    dept_name=models.CharField(max_length=10)
    def __str__(self):
        return self.dept_name

class Student(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    dept=models.ForeignKey('Department',on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=10)
    description = models.CharField(max_length=30)
    date_field = models.DateField()
