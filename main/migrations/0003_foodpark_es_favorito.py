# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_foodpark_descripcion_foodpark'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodpark',
            name='es_favorito',
            field=models.BooleanField(default=False),
        ),
    ]
