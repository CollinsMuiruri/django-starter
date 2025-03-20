# Generated by Django 5.1.7 on 2025-03-16 20:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("shule_app", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("f_name", models.CharField(max_length=100, verbose_name="First Name")),
                (
                    "m_name",
                    models.CharField(max_length=100, verbose_name="Middle Name"),
                ),
                ("l_name", models.CharField(max_length=100, verbose_name="Last Name")),
                (
                    "student_id",
                    models.CharField(editable=False, max_length=10, unique=True),
                ),
                ("email", models.CharField(max_length=100, null=True, unique=True)),
                ("join_date", models.DateField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "class_grade",
                    models.ManyToManyField(
                        related_name="students", to="shule_app.classgrade"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Teacher",
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
                ("f_name", models.CharField(max_length=100, verbose_name="First Name")),
                (
                    "m_name",
                    models.CharField(max_length=100, verbose_name="Middle Name"),
                ),
                ("l_name", models.CharField(max_length=100, verbose_name="Last Name")),
                (
                    "teacher_id",
                    models.CharField(editable=False, max_length=10, unique=True),
                ),
                ("email", models.CharField(max_length=100, null=True, unique=True)),
                ("join_date", models.DateField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "subjects",
                    models.ManyToManyField(
                        related_name="teachers", to="shule_app.subject"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
