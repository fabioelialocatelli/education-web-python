from django.db import models

# Create your models here.

class inmueble(models.Model):
    zona = models.CharField(max_length=50)
    descrip = models.TextField()
    precio = models.FloatField()
    ref = models.IntegerField()
    