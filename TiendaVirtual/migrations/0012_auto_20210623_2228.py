# Generated by Django 3.2.3 on 2021-06-23 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaVirtual', '0011_remove_producto_agricultor'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precioKilo',
            field=models.IntegerField(null=True, verbose_name='Precio Kg'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=100, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank='True', null=True, upload_to='productos', verbose_name='Fotografia (Opcional)'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombreProducto',
            field=models.CharField(max_length=20, verbose_name='Nombre Producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precioKiloMayorista',
            field=models.IntegerField(blank=True, null='true', verbose_name='Precio Kg Mayorista'),
        ),
    ]