from django.db import models
from django.utils import timezone

class Usuario(models.Model):
	# id = models.AutoField(primary_key=True)
	apellido = models.CharField(max_length=30)
	nombre = models.CharField(max_length=30)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=12)
	email = models.EmailField()
	domicilio = models.TextField()

	def __str__(self):
		return	'{} {}'.format(self.apellido, self.nombre)

