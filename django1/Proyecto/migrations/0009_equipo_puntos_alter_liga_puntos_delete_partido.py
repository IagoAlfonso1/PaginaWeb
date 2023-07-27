# Generated by Django 4.0.5 on 2022-07-05 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto', '0008_partido_puntos'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='puntos',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='liga',
            name='puntos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proyecto.equipo', verbose_name='Puntos Equipo'),
        ),
        migrations.DeleteModel(
            name='Partido',
        ),
    ]
