# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodpark',
            name='descripcion_foodpark',
            field=models.CharField(max_length=240, default='Descripcion foodpark'),
            preserve_default=False,
        ),
    ]
