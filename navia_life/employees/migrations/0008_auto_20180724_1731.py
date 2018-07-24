# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-24 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_auto_20180724_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadreport',
            name='share_with',
        ),
        migrations.AddField(
            model_name='uploadreport',
            name='share_with_docs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='uploadreport',
            name='share_with_nurse',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='uploadreport',
            name='share_with_receptionist',
            field=models.BooleanField(default=False),
        ),
    ]
