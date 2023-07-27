from django.db import models
from django.forms import ModelForm

# Create your models here.
class Objeto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=100)
    puntos = models.PositiveIntegerField(null=False)
    def __str__(self):
        return "Puntos: {}".format(self.puntos)

class Jugador(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    puntos = models.PositiveIntegerField(null=False)
    def __str__(self):
        return "PuntosJugador {}" .format(self.puntos)

class Equipo(models.Model):
    nombre = models.CharField(max_length=100,null=False)
    jugadores = models.ManyToManyField(Jugador)
    puntos = models.PositiveIntegerField(null=False, default=0)

class Persona(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    DNI = models.PositiveIntegerField(null=False, unique=True)
    NombreEquipo = models.CharField(max_length=100, null=False)
    contra = models.CharField(max_length=100, null=False)

    def nombre_completo(self):
        return "{} {}, {}" .format(self.apellido,self.nombre, self.DNI)
    def __str__(self):
        return self.nombre_completo()

class Liga(models.Model):
    puntos = models.PositiveIntegerField(null=False, default=0)

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'DNI', 'NombreEquipo', 'contra']
