# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-27 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chroniFic', '0004_auto_20171027_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialist',
            name='available_from',
            field=models.DateTimeField(auto_now_add=True, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialist',
            name='available_to',
            field=models.DateTimeField(auto_now_add=True, default=''),
            preserve_default=False,
        ),
    ]
