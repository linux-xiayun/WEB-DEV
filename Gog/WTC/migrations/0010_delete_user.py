# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WTC', '0009_auto_20171025_1533'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
