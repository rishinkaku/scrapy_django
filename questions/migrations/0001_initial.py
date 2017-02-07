# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-07 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('identifier', models.CharField(max_length=256)),
                ('url', models.CharField(max_length=1024)),
            ],
        ),
    ]
