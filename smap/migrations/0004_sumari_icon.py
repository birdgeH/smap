# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-10 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smap', '0003_auto_20170115_0336'),
    ]

    operations = [
        migrations.AddField(
            model_name='sumari',
            name='icon',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
