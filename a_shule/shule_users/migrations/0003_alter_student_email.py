# Generated by Django 5.1.7 on 2025-03-16 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shule_users', '0002_remove_student_class_grade_student_class_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=100, null=True, unique=True),
        ),
    ]
