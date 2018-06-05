# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-05 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('link_url', models.TextField(blank=True)),
                ('description', models.CharField(max_length=200)),
                ('screenshot', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
    ]
