# Generated by Django 4.0.5 on 2022-07-05 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto', '0007_alter_equipo_nombre_alter_jugador_apellido_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='puntos',
            field=models.PositiveIntegerField(default=0),
        ),
    ]