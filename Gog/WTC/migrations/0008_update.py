# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WTC', '0007_auto_20171015_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('items_id', models.IntegerField()),
                ('items_name', models.CharField(max_length=50)),
                ('items_place', models.CharField(max_length=50, null=True)),
                ('items_system', models.CharField(max_length=50, null=True)),
                ('items_resource', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
