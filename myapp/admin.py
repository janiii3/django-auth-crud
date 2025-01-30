from django.contrib import admin
from .models import Project, Task, Task2
# Register your models here.

admin.site.register(Project) #con esto resgistro el modulo proyecto en el panel de admin
admin.site.register(Task)
admin.site.register(Task2)