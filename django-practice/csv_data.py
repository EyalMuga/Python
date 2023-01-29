import os
import django
import csv
from datetime import datetime, date, time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "companies.settings")
django.setup()


from company.models import Employee,Person,Company


with open("/Users/MUGA/Downloads/companies.csv","r") as file:  
    company_file = csv.DictReader(file, delimiter=',')    
    for item in company_file:       
        company = Company(
        id = item["id"],
        name = item["company_name"],
        country = item["country"],
        city = item["city"],
        address = item["address"],
        phone = item["phone_num"])
        company.save()

with open("/Users/MUGA/Downloads/employees.csv","r") as file:
    employee_file = csv.DictReader(file, delimiter=',')
    for item in employee_file:
        person_id = item["person_id"]
        if Person.objects.filter(id=person_id).exists():
            employee = Employee(
            id = item["id"],
            company_id= item["company_id"],
            person_id = person_id,
            job_title = item["job_title"],
            is_current_job = item["is_current_job"].title(),
            company_email = item["company_email"])
            employee.save()
        else:
            # Handle the case where the person does not exist
            pass



with open("/Users/MUGA/Downloads/persons.csv","r") as file:
    person_file = csv.DictReader(file, delimiter=',')
    for item in person_file:
        birth_date = datetime.strptime(item["birth_date"], "%m/%d/%Y").strftime("%Y-%m-%d")
        person = Person(
        id = item["id"],
        first_name = item["first_name"],
        last_name = item["last_name"],
        email = item["personal_email"],
        gender = item["gender"],
        birth_date = birth_date,
        age = datetime.now().year - int(birth_date.split("-")[0]))
        person.save()





