from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=256,null=False,blank=False)
    country = models.CharField(max_length=256,null=False,blank=False)
    city = models.CharField(max_length=256,null=False,blank=False)
    address = models.CharField(max_length=256,null=False,blank=False)
    phone = models.CharField(max_length = 256,null=False,blank=False)

    class Meta:
        db_table = "company"

class Person(models.Model):
    first_name = models.CharField(max_length=256,null=False,blank=False)
    last_name = models.CharField(max_length=256,null=False,blank=False)
    email = models.EmailField(max_length=256,null=False,blank=False)
    gender = models.CharField(max_length=256,null=False,blank=False)
    birth_date = models.DateField(null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)

    class Meta:
        db_table = "person"

class Employee(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    job_title = models.CharField(max_length=256,null=False,blank=False)
    is_current_job = models.BooleanField(default=True)
    company_email = models.EmailField(max_length=256,null=False,blank=False)

    class Meta:
        db_table = "employee"







