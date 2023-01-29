import django
import os
import datetime 
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "companies.settings")
django.setup()

from company.models import Employee,Person,Company

def get_person_name_by_id(id)->str:
    person = Person.objects.get(id=id)
    return person.first_name + " " + person.last_name

# print(get_person_name_by_id(1))

def get_person_by_age(age):
    persons = Person.objects.filter(age=age)
    for person in persons:
        return person.first_name + " " + person.last_name

# print(get_person_by_age(58))

def get_company_by_country(country):
    companies = Company.objects.filter(country=country)
    for company in companies:
        print(company.name)

# print(get_company_by_country("China"))

def get_company_employee(company_id):
    employees = Employee.objects.filter(company_id=company_id)
    for employee in employees:
        print(get_person_name_by_id(employee.person_id))

# print(get_company_employee(1))

def get_employee_by_job_title(job_title):
    employees = Employee.objects.filter(job_title=job_title)
    for employee in employees:
        print(get_person_name_by_id(employee.person_id))

print(get_employee_by_job_title("VP Sales"))

def get_person_jobs(person_id: int) -> list[dict[str, str]]:
    """
    Given person_id, return list of dictionaries that map from company name to job title
    param person_id:
    return:
"""
    jobs = []
    employees = Employee.objects.filter(person_id=person_id)
    for employee in employees:
        company = Company.objects.get(id=employee.company_id)
        jobs.append({"company_name": company.name, "job_title": employee.job_title})
    return jobs

# print(get_person_jobs(23))




