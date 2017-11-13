# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WTC', '0010_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='update_items',
            name='items_id',
        ),
        migrations.AlterField(
            model_name='update_items',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
