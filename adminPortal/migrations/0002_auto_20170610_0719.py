# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 07:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminPortal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumerUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumer_is_admin', models.BooleanField(default=False)),
                ('consumer_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='adminuser',
            name='admin_user',
        ),
        migrations.DeleteModel(
            name='AdminUser',
        ),
    ]
