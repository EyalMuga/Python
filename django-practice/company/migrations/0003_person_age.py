# Generated by Django 4.1.5 on 2023-01-29 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_remove_employee_name_remove_employee_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]