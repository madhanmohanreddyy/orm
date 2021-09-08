from django.http import request
from django.shortcuts import render



# Create your views here.
from app.models import *
from django.db.models import Q

def display_topic(request):
    companys=COMPANY.objects.all()
    return render(request,'display_topic.html',context={'companies':companys})

def display_employee(request):
    employees=EMPLOYEE.objects.all() #all columns
    #employees=EMPLOYEE.objects.exclude(name='Thomas') #except that remainin all
    #employees=EMPLOYEE.objects.all().order_by('name')  #for ascending
    #employees=EMPLOYEE.objects.all().order_by('-name') #for descending
    #employees=EMPLOYEE.objects.all().order_by(length('name'))
    #employees=EMPLOYEE.objects.filter(Q(company_name='oracle')&Q(name='Robert')) #multiple conditions inside filter
    #employees=EMPLOYEE.objects.filter(name__in=['Robert','Thomas'])  #eliminating multiple or's
    #employees=EMPLOYEE.objects.filter(name__regex=r'T[a-zA_Z]{5}')   #regular expressions
    return render(request,'display_employee.html',context={'employees':employees})

def display_record(request):
    records=RECORD.objects.all()
    records=RECORD.objects.filter(date__lte='1995-11-11')
    records=RECORD.objects.filter(date__gte='1995-11-11')
    records=RECORD.objects.filter(date__lt='1995-11-11')
    records=RECORD.objects.filter(date__gt='1995-11-11')
    records=RECORD.objects.filter(date='1995-11-11')
    d={'records':records}
    return render(request,'display_records.html',d) 

def delete_employee(request):
    employees=EMPLOYEE.objects.all().delete()
    return render(request,'display_employee.html')

def update_employee(request):
    companies=COMPANY.objects.get_or_create(company_name='tcs')[0]
    companies.save()
    employees=EMPLOYEE.objects.update_or_create(company_name='tcs',defaults={'company_name':companies,'name':'chandra','age':22,'url':'http://chandra.com/'})
    employees=EMPLOYEE.objects.all() 
    d={'employees':employees}
    return render(request,'display_employee.html',d )     
