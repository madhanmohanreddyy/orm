import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','orm1.settings')

import django
django.setup()
from app.models import *
import random
from faker import Faker
f=Faker()

list=['oracle','google','microsoft','amazon']
def add_company():
    c=COMPANY.objects.get_or_create(company_name=random.choice(list))[0]
    c.save()
    return c

def add_employee(name,age,url):
    c=add_company()
    e=EMPLOYEE.objects.get_or_create(company_name=c,name=name,age=age,url=url)[0]
    e.save()
    return e

def add_records(name,age,url,date):
    name=add_employee(name,age,url)
    a=RECORD.objects.get_or_create(name=name,date=date)[0] 
    a.save()

def add_data(n):
    for i in range(n):
        fake_name=f.first_name()
        fake_age=f.pyint()
        fake_url=f.url()
        fake_date=f.date()

        add_records(fake_name,fake_age,fake_url,fake_date)

if __name__=='__main__':
    n=int(input('enter n value'))
    print('population is started')
    add_data(n)
    print('populated successfully')

