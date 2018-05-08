# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid

class Person(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4(), null=False, editable=False)
    fname = models.CharField(max_length=128, null=False, verbose_name="First Name")
    lname = models.CharField(max_length=128, null=False, verbose_name="Last Name")
    age = models.IntegerField(null=False)
