from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model): #controlar datos que puedo estar guardando en una tabla
    name  = models.CharField(max_length=200) # ahora mismo estoy creando una tabla llamada project donde puedes meter un nombre string de maximo 200 caracteres

    def __str__(self):
        return self.name

class Task(models.Model): # cuando creamos unatarea le tenemos que decir a que proyecto pertenece
    title = models.CharField(max_length=200) # charfield mas para textos cortos
    description = models.TextField(blank=True) # para textos mas largos, en este caso sin limite
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # AQUI PONGO CON QUE TABLA ESTA RELACIONADA!!! cuando se elimine un dato se eliminen en cascada
    done = models.BooleanField() # por defecto todas false
    def __str__(self):
        return self.title + ' - ' + self.project.name

class Task2(models.Model): # cuando creamos unatarea le tenemos que decir a que proyecto pertenece
    title = models.CharField(max_length=200) # charfield mas para textos cortos
    description = models.TextField(blank=True) # para textos mas largos, en este caso sin limite
    importance = models.BooleanField(default=False) # por defecto todas false
    datecompleted = models.DateTimeField(null=True) # para fechas y hora de creacion de la tarea, en este caso vacio al principio
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + self.user.username

    
