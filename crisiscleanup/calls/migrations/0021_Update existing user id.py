# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-19 22:48
from __future__ import unicode_literals

from django.db import migrations


def update_user(apps, schema_editor):
    User = apps.get_model('calls', 'User')
    for user in User.objects.all():
        if (user.name == 'Sean Fisher'):
            user.cc_id = 7748
            user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0020_Remove user PK'),
    ]

    operations = [
        migrations.RunPython(update_user),
    ]