from django.db import models, transaction
from django.contrib.auth.models import User
from shule_app.models import Subject, ClassGrade
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from datetime import datetime


# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=100, verbose_name="First Name")
    m_name = models.CharField(max_length=100, verbose_name="Middle Name")
    l_name = models.CharField(max_length=100, verbose_name="Last Name")
    student_id = models.CharField(max_length=10, unique=True, editable=False)
    email = models.EmailField(max_length=100, null=True, unique=True)
    # phone_number = models.IntegerField(default=1)
    join_date = models.DateField(null=False)
    class_grade = models.ForeignKey(ClassGrade, on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"

    def generate_student_id(self):
        if not self.created_on:
            self.created_on = datetime.now()

        year = self.created_on.strftime("%y")  # Last two digits of the year (e.g., 23 for 2023)

        # Find the last student_id for the current year and month
        last_student = (
            Student.objects.filter(student_id__startswith=f"S{year}")
            .order_by("-student_id")
            .first()
        )

        if last_student:
            # Extract the incrementing number and increment it
            last_number = int(last_student.student_id[-3:])  # Last 3 digits (e.g., 001)
            new_number = last_number + 1
        else:
            # Start from 001 if no student exists for this year and month
            new_number = 1

        # Format the new student_id (e.g., S2310001)
        return f"S{year}{new_number:03d}"

    @transaction.atomic
    def save(self, *args, **kwargs):
        if not self.student_id:
            # Generate student_id within a transaction
            retries = 3  # Number of retries in case of IntegrityError
            for _ in range(retries):
                try:
                    self.student_id = self.generate_student_id()
                    super().save(*args, **kwargs)
                    break  # Exit the loop if save is successful
                except IntegrityError:
                    # If a duplicate student_id occurs (due to concurrency), retry
                    continue
            else:
                raise ValidationError(
                    "Failed to generate a unique student_id after multiple attempts."
                )
        else:
            super().save(*args, **kwargs)


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=100, verbose_name="First Name")
    m_name = models.CharField(max_length=100, verbose_name="Middle Name")
    l_name = models.CharField(max_length=100, verbose_name="Last Name")
    teacher_id = models.CharField(max_length=10, unique=True, editable=False)
    email = models.CharField(max_length=100, null=True, unique=True)
    phone_number = models.IntegerField(default=None)
    join_date = models.DateField(null=False)
    is_class_teacher = models.BooleanField(default=False)
    class_grade = models.ForeignKey(ClassGrade, on_delete=models.CASCADE, null=True)
    subjects = models.ManyToManyField(Subject, related_name="teachers")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"

    def generate_teacher_id(self):
        if not self.created_on:
            self.created_on = datetime.now()
        year = self.created_on.strftime("%y")  # Last two digits of the year (e.g., 23 for 2023)

        # Find the last teacher_id for the current year and month
        last_teacher = (
            Teacher.objects.filter(teacher_id__startswith=f"T{year}")
            .order_by("-teacher_id")
            .first()
        )

        if last_teacher:
            # Extract the incrementing number and increment it
            last_number = int(last_teacher.teacher_id[-3:])  # Last 3 digits (e.g., 001)
            new_number = last_number + 1
        else:
            # Start from 001 if no teacher exists for this year and month
            new_number = 1

        # Format the new teacher_id (e.g., T2310001)
        return f"T{year}{new_number:03d}"

    @transaction.atomic
    def save(self, *args, **kwargs):
        if not self.teacher_id:
            # Generate teacher_id within a transaction
            retries = 3  # Number of retries in case of IntegrityError
            for _ in range(retries):
                try:
                    self.teacher_id = self.generate_teacher_id()
                    super().save(*args, **kwargs)
                    break  # Exit the loop if save is successful
                except IntegrityError:
                    # If a duplicate teacher_id occurs (due to concurrency), retry
                    continue
            else:
                raise ValidationError(
                    "Failed to generate a unique teacher_id after multiple attempts."
                )
        else:
            super().save(*args, **kwargs)


class ParentOrGuardian(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=100, verbose_name="First Name")
    m_name = models.CharField(max_length=100, verbose_name="Middle Name")
    l_name = models.CharField(max_length=100, verbose_name="Last Name")
    parent_id = models.CharField(max_length=10, unique=True)
    GENDER_OPTIONS=[
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    gender = models.CharField(choices=GENDER_OPTIONS, max_length=10)
    child = models.ForeignKey(Student, on_delete=models.CASCADE)
    phone_number = models.IntegerField(default=None)
    other_phone_number = models.IntegerField(null=True)
    email = models.EmailField(max_length=50)
    RELATION_OPTIONS = [
        ("Father", "Father"),
        ("Mother", "Mother"),
        ("Guardian", "Guardian"),
    ]
    relation = models.CharField(max_length=20, choices=RELATION_OPTIONS)

    def __str__(self):
        return(self.f_name)