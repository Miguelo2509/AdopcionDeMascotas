from django.db import models
from django.utils import timezone
from apps.usuario.models import Usuario

class Vacuna(models.Model):
	nombre=models.CharField(max_length=30)

	def __str__(self):
		return '{}'.format(self.nombre)

class Mascota(models.Model):
	nombre = models.CharField(max_length=30)
	especie = models.CharField(max_length=30)
	raza = models.CharField(max_length=30)
	sexo = models.CharField(max_length=30)
	fechaNac = models.DateTimeField(blank=True, null=True)
	usuario = models.ForeignKey(Usuario, null=True,blank=True, on_delete=models.CASCADE)
	vacuna = models.ManyToManyField(Vacuna)

# id = models.AutoField(primary_key=True)
# duenio = models.ForeignKey('auth.User', on_delete=models.CASCADE)

#    def publish(self):
#        self.published_date = timezone.now()
#        self.save()

#    def __str__(self):
#        return self.title