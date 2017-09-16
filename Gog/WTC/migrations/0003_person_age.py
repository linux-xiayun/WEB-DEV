# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WTC', '0002_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
