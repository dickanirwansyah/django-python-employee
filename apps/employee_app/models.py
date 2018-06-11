# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# untuk migration database bikin model schema

#table employee_app_employee
class employee(models.Model):
    name_employee = models.CharField(max_length=45)
    email_employee = models.CharField(max_length=45, unique=True)
    position_employee = models.CharField(max_length=45)
    ages_employee = models.IntegerField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

