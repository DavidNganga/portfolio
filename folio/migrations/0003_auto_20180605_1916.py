# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-05 19:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0002_auto_20180605_1848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='image_url',
            new_name='image',
        ),
    ]