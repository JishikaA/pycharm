from django.contrib import admin

from app import models

# Register your models here.
admin.site.register(models.Test)

# admin.site.register(models.Department)
# admin.site.register(models.Student)
admin.site.register(models.Todo)
