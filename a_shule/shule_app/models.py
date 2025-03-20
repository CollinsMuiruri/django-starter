from django.db import models


# Create your models here.


class Term(models.Model):
    TERM_CHOICES = [
        ("Term 1", "Term 1"),
        ("Term 2", "Term 2"),
        ("Term 3", "Term 3"),
    ]

    name = models.CharField(max_length=10, choices=TERM_CHOICES, unique=True)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)

    def __str__(self):
        return f"{self.name}"

class AcademicYear(models.Model):
    year = models.IntegerField(blank=False)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    term = models.ManyToManyField(Term, related_name='academicyears')

    def __str__(self):
        return f"Year {self.year}"

class Stream(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ClassGrade(models.Model):
    GRADE_CHOICES = [
        ("Grade 1", "Grade 1"),
        ("Grade 2", "Grade 2"),
        ("Grade 3", "Grade 3"),
        ("Grade 4", "Grade 4"),
        ("Grade 5", "Grade 5"),
        ("Grade 6", "Grade 6"),
        ("Grade 7", "Grade 7"),
        ("Grade 8", "Grade 8"),
        ("Grade 9", "Grade 9"),
    ]
    name = models.CharField(max_length=10, choices=GRADE_CHOICES, unique=True)
    stream = models.ManyToManyField(Stream, related_name='classgrades')
    ac_year = models.ForeignKey(AcademicYear, on_delete=models.PROTECT, verbose_name="Academic Year", null=True)

    def __str__(self):
        return f"{self.name}"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Assignment(models.Model):
    subject = models.ForeignKey(Subject, related_name="assignments", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    points = models.IntegerField()
    due_date = models.DateField(null=True)

    def __str__(self):
        return self.name
