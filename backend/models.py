# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class picture(models.Model):
    name = models.CharField(max_length=64)
    path = models.CharField(max_length=64)
    result = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name