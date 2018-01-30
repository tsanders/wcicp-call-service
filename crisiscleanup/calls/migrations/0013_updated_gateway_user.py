# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-30 03:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0012_auto_20180123_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_used_gateway',
        ),
        migrations.AddField(
            model_name='gateway',
            name='agent_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='gateway',
            name='agent_password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='gateway',
            name='agent_username',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gateway',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='calls.Gateway'),
        ),
    ]
