# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-11-13 16:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matkul', '0005_auto_20221114_0000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='kelas',
            new_name='mata_kuliah',
        ),
        migrations.RemoveField(
            model_name='post',
            name='mk',
        ),
        migrations.DeleteModel(
            name='mk',
        ),
    ]
