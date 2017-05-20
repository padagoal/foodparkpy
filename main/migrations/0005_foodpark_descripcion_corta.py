# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_local_es_recomendado'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodpark',
            name='descripcion_corta',
            field=models.CharField(max_length=240, default='Descripcion Corta'),
        ),
    ]
