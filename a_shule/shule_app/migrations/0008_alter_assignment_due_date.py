# Generated by Django 5.1.7 on 2025-03-16 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shule_app', '0007_alter_assignment_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateField(null=True),
        ),
    ]
