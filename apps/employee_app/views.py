# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here. sama aja seperti controller pada spring-boot

def index(request):
    return render(request, 'employee_app/index.html')
