# Generated by Django 5.1.6 on 2025-02-26 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_appoitementstatus_appointment_appointementstatus_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='appointementFor',
            new_name='appointmentFor',
        ),
    ]
