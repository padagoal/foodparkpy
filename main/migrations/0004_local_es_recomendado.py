# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_foodpark_es_favorito'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='es_recomendado',
            field=models.BooleanField(default=False),
        ),
    ]
