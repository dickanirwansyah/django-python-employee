# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import employee


# views controller

def index(request):
    employees = employee.objects.all()
    context = {'employees':employees}
    return render(request, 'employee_app/index.html', context)

def add_new_employee(request):
    return render(request, 'employee_app/add_employee.html')

def get_employee(request, id):
    emp = employee.objects.get(id=id)
    context = {"emp":emp}
    return render(request, 'employee_app/update_employee.html', context)

def destroy_employee(request, id):
    emp = employee.objects.get(id = id)
    emp.delete()
    return redirect('/')

def save_employee(request):
    print request.POST
    emp = employee(
        name_employee = request.POST['name_employee'],
        email_employee = request.POST['email_employee'],
        position_employee = request.POST['position_employee'],
        ages_employee = request.POST['ages_employee']
    )
    emp.save()
    return redirect('/')

def update_employee(request, id):
    emp = employee.objects.get(id=id)
    emp.name_employee= request.POST['name_employee']
    emp.email_employee = request.POST['email_employee']
    emp.position_employee = request.POST['position_employee']
    emp.ages_employee = request.POST['ages_employee']
    emp.save()
    return redirect('/')

