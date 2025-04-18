# Generated by Django 5.1.1 on 2025-02-20 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0002_delete_usermessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientCredientialsModel',
            fields=[
                ('patientId', models.AutoField(primary_key=True, serialize=False)),
                ('patient_name', models.CharField(max_length=50)),
                ('patient_emailId', models.EmailField(max_length=254)),
                ('patient_password', models.CharField(max_length=30)),
            ],
        ),
    ]
