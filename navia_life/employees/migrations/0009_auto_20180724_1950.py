# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-24 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_auto_20180724_1731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadreport',
            old_name='share_with_docs',
            new_name='Doctor',
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='type',
            field=models.CharField(choices=[(b'Doctor', b'Doctor'), (b'Nurse', b'Nurse'), (b'Receptionist', b'Receptionist')], max_length=12),
        ),
    ]
