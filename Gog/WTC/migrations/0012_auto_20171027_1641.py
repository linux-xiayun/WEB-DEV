# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WTC', '0011_auto_20171027_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update_items',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True),
        ),
    ]
