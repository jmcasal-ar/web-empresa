# Generated by Django 2.2.4 on 2020-01-16 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación'),
        ),
        migrations.AlterField(
            model_name='service',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación'),
        ),
    ]
