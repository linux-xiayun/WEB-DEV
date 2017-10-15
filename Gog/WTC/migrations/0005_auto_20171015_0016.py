# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WTC', '0004_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('public_ip', models.CharField(verbose_name='公网IP', max_length=100)),
                ('intranet_ip', models.CharField(verbose_name='内网IP', max_length=100)),
                ('host_name', models.CharField(verbose_name='主机名', max_length=50)),
                ('os', models.CharField(verbose_name='操作系统', max_length=50)),
                ('cpu_model', models.CharField(verbose_name='CPU型号', max_length=100)),
                ('cpu_thread_number', models.PositiveIntegerField(verbose_name='CPU线程数')),
                ('memory', models.CharField(verbose_name='内存', max_length=50)),
                ('disk', models.TextField(verbose_name='磁盘')),
                ('minion_id', models.CharField(null=True, max_length=50)),
            ],
            options={
                'db_table': '"asset_info"',
            },
        ),
        migrations.CreateModel(
            name='Charts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('insert_time', models.CharField(max_length=50)),
                ('pv_number', models.IntegerField()),
                ('uv_number', models.IntegerField()),
            ],
            options={
                'db_table': '"web_access_count"',
            },
        ),
        migrations.CreateModel(
            name='MinionInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('key_status', models.CharField(max_length=50)),
                ('port', models.IntegerField()),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('asset_info', models.ManyToManyField(to='WTC.AssetInfo')),
            ],
        ),
        migrations.AlterModelTable(
            name='user',
            table='"user"',
        ),
    ]
