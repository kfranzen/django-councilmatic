# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-12 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('councilmatic_core', '0013_auto_20161012_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='shape',
            field=models.TextField(blank=True, null=True),
        ),
    ]