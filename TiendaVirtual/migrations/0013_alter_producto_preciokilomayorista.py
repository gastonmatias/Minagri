# Generated by Django 3.2.3 on 2021-06-24 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaVirtual', '0012_auto_20210623_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precioKiloMayorista',
            field=models.IntegerField(null='true', verbose_name='Precio Kg Mayorista'),
        ),
    ]
