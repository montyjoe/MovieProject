# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-27 01:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User_app', '0008_auto_20170827_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='User_app.User'),
        ),
    ]
