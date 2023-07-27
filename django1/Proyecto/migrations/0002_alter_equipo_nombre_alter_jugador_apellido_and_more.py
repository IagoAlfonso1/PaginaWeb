# Generated by Django 4.0.5 on 2022-06-26 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='nombre',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nombre de Equipo'),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='apellido',
            field=models.CharField(max_length=100, unique=True, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='nombre',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='NombreEquipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proyecto.equipo'),
        ),
    ]