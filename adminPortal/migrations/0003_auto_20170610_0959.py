# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPortal', '0002_auto_20170610_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_id',
            field=models.IntegerField(max_length=40),
        ),
    ]