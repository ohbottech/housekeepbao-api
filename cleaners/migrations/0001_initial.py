# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cleaner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('phone', models.IntegerField()),
                ('email', models.TextField()),
                ('password', models.CharField(max_length=50)),
                ('gender', models.TextField()),
                ('description', models.TextField()),
                ('last_modify_date', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cleaner',
            },
        ),
    ]
