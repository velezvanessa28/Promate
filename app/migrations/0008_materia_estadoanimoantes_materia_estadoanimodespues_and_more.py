# Generated by Django 4.1.2 on 2023-04-05 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_notas_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='estadoAnimoAntes',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='materia',
            name='estadoAnimoDespues',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='materia',
            name='horario',
            field=models.TimeField(default=datetime.time(9, 0)),
        ),
    ]