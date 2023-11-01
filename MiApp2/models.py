from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Trabajo(models.Model):
    nombre=models.CharField(max_length=40)
    sueldo = models.IntegerField()

    def __str__(self):
        return f'Nombre: {self.nombre}, Sueldo: {self.sueldo}'
    
class Empleado(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}, Profesion: {self.profesion}'
    
class Cliente(models.Model):
    nombre= models.CharField(max_length=40) 
    apellido= models.CharField(max_length=40)
    email= models.EmailField()

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}'
    
class Avatar(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	imagen = models.ImageField(upload_to='media/avatares', null=True, blank = True)
	def __str__(self):
		return f'{self.user.username}'