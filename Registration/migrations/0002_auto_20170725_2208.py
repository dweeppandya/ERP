# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='faculty_code',
            field=models.AutoField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
