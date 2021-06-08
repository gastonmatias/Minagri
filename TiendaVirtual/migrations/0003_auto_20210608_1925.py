# Generated by Django 3.2.3 on 2021-06-08 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaVirtual', '0002_auto_20210607_0003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agricultor',
            options={'verbose_name': 'Agricultor', 'verbose_name_plural': 'Agricultores'},
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterField(
            model_name='agricultor',
            name='appaterno',
            field=models.CharField(max_length=20, verbose_name='Apellido Paterno'),
        ),
    ]