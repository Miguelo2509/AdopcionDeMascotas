from django.db import models
from django.utils import timezone

class Mascota(models.Model):
	pass
	# id = models.AutoField(primary_key=True)
	# nombre = models.CharField(max_length=30)
	# duenio = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	# especie = models.CharField(max_length=30)
	# raza = models.CharField(max_length=30)
	# sexo = models.CharField(max_length=30)
	# fechaNac = models.DateTimeField(
 #            blank=True, null=True)

 #    def publish(self):
 #        self.published_date = timezone.now()
 #        self.save()

 #    def __str__(self):
 #        return self.title
