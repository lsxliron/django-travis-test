# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-06 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=128)),
                ('lname', models.CharField(max_length=128)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
