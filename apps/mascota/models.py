from django.db import models
from django.utils import timezone

class Mascota(models.Model):
	nombre = models.CharField(max_length=30)
	especie = models.CharField(max_length=30)
	raza = models.CharField(max_length=30)
	sexo = models.CharField(max_length=30)
	fechaNac = models.DateTimeField(blank=True, null=True)

# id = models.AutoField(primary_key=True)
# duenio = models.ForeignKey('auth.User', on_delete=models.CASCADE)

 #    def publish(self):
 #        self.published_date = timezone.now()
 #        self.save()

 #    def __str__(self):
 #        return self.title