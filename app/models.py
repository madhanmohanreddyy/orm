from django.db import models

# Create your models here.
class COMPANY(models.Model):
    company_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.company_name

class EMPLOYEE(models.Model):
    company_name=models.ForeignKey(COMPANY,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,primary_key=True)
    age=models.IntegerField()
    url=models.URLField()

    def __str__(self):
        return self.name

class RECORD(models.Model):
    name=models.ForeignKey(EMPLOYEE,on_delete=models.CASCADE)
    date=models.DateField()

    