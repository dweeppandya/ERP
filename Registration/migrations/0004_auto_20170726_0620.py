# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-26 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0003_auto_20170726_0557'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='branch',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='year',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]