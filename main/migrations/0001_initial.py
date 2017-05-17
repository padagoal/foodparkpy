# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre_ciudad', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Foodpark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre_foodpark', models.CharField(max_length=25)),
                ('direccion_foodpark', models.CharField(max_length=150)),
                ('lon_foodpark', models.CharField(max_length=25)),
                ('lat_foodpark', models.CharField(max_length=25)),
                ('logo', models.FileField(upload_to='')),
                ('telefono', models.CharField(max_length=25)),
                ('facebook', models.CharField(max_length=200)),
                ('instagram', models.CharField(max_length=200)),
                ('ciudad', models.ManyToManyField(to='main.Ciudad')),
            ],
            options={
                'verbose_name': 'Foodpark',
                'verbose_name_plural': 'Foodparks',
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre_local', models.CharField(max_length=25)),
                ('foto_local', models.FileField(upload_to='')),
                ('facebook', models.CharField(max_length=200)),
                ('instagram', models.CharField(max_length=200)),
                ('foodpark', models.ManyToManyField(to='main.Foodpark')),
            ],
            options={
                'verbose_name': 'Local',
                'verbose_name_plural': 'Locales',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre_pais', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Pais',
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre_plato', models.CharField(max_length=25)),
                ('descripcion_plato', models.CharField(max_length=240)),
                ('ingredientes_plato', models.CharField(max_length=240)),
                ('precio', models.CharField(max_length=25)),
                ('foto_plato', models.FileField(upload_to='')),
                ('local', models.ManyToManyField(to='main.Local')),
            ],
            options={
                'verbose_name': 'Plato',
                'verbose_name_plural': 'Platos',
            },
        ),
        migrations.AddField(
            model_name='ciudad',
            name='pais',
            field=models.ManyToManyField(to='main.Pais'),
        ),
    ]
