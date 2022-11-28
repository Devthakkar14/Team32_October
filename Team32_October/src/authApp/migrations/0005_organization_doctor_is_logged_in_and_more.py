# Generated by Django 4.1.3 on 2022-11-28 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authApp", "0004_user_author"),
    ]

    operations = [
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("Organization_Type", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=500, unique=True)),
                ("username", models.CharField(max_length=255, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("is_logged_in", models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name="doctor",
            name="is_logged_in",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="department",
            field=models.CharField(
                choices=[
                    ("Cardiologist", "Cardiologist"),
                    ("Dermatologists", "Dermatologists"),
                    (
                        "Emergency Medicine Specialists",
                        "Emergency Medicine Specialists",
                    ),
                    ("Allergists/Immunologists", "Allergists/Immunologists"),
                    ("Surgeon", "Surgeon"),
                ],
                max_length=255,
            ),
        ),
    ]