# Generated by Django 4.1.3 on 2022-11-28 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authApp", "0005_organization_doctor_is_logged_in_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="author",
        ),
    ]
