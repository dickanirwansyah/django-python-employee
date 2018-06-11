# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import employee


# Create your views here. sama aja seperti controller pada spring-boot

def index(request):
    employees = employee.objects.all()
    context = {'employees':employees}
    return render(request, 'employee_app/index.html', context)

def add_new_employee(request):
    return render(request, 'employee_app/add_employee.html')


