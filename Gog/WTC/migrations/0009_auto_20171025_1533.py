# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WTC', '0008_update'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Update',
            new_name='Update_items',
        ),
    ]
