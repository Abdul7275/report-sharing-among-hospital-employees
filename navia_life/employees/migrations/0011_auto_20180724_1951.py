# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-24 14:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0010_auto_20180724_1950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadreport',
            old_name='share_with_receptionist',
            new_name='Receptionist',
        ),
    ]
