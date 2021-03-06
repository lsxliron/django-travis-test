# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-06 17:47
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_person_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='fname',
            field=models.CharField(max_length=128, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='lname',
            field=models.CharField(max_length=128, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('d2e962a9-7644-4d4a-b2e5-c405304138d7'), editable=False),
        ),
    ]
