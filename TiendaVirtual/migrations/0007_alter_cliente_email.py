# Generated by Django 3.2.3 on 2021-06-11 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaVirtual', '0006_auto_20210611_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Correo electronico'),
        ),
    ]