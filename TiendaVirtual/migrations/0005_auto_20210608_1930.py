# Generated by Django 3.2.3 on 2021-06-08 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaVirtual', '0004_auto_20210608_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agricultor',
            name='nombreComercial',
            field=models.CharField(blank=True, max_length=25, null='true', verbose_name='Nombre Comercial'),
        ),
        migrations.AlterField(
            model_name='agricultor',
            name='telefono1',
            field=models.CharField(max_length=15, verbose_name='Telefono 1'),
        ),
        migrations.AlterField(
            model_name='agricultor',
            name='telefono2',
            field=models.CharField(blank=True, max_length=15, null='true', verbose_name='Telefono 2'),
        ),
    ]
