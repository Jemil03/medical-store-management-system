# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2021-04-14 15:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharma', '0017_auto_20171111_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='c_id',
        ),
        migrations.RemoveField(
            model_name='dealer',
            name='d_id',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='p_id',
        ),
    ]
