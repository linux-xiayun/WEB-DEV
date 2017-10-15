# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WTC', '0003_person_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(unique=True, max_length=50, verbose_name='用户名')),
                ('email', models.EmailField(max_length=150)),
                ('register_time', models.DateTimeField(null=True, verbose_name='注册时间')),
                ('last_login_time', models.DateTimeField(null=True, verbose_name='最后登录时间')),
                ('last_login_ip', models.GenericIPAddressField(null=True, verbose_name='最后登录IP')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
