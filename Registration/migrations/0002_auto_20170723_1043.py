# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-23 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='email',
            field=models.EmailField(default='test@test.com', max_length=100),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='mobile',
            field=models.BigIntegerField(default=8557),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='nationality',
            field=models.CharField(default='Test', max_length=50),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='religion',
            field=models.CharField(default='Test', max_length=20),
        ),
    ]
