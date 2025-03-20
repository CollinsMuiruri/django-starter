from django.contrib import admin
from .models import AcademicYear, Term, ClassGrade, Assignment, Subject, Stream

from unfold.admin import ModelAdmin


@admin.register(AcademicYear)
class AcademicYearAdmin(ModelAdmin):
    search_fields = ["year"]
    autocomplete_fields = ["term"]



@admin.register(Term)
class TermAdmin(ModelAdmin):
    search_fields = ["name"]


@admin.register(ClassGrade)
class ClassGradeAdmin(ModelAdmin):
    autocomplete_fields = ["stream", "ac_year"]
    search_fields = ["name"]


@admin.register(Assignment)
class AssignmentAdmin(ModelAdmin):
    autocomplete_fields = ["subject"]


@admin.register(Subject)
class SubjectAdmin(ModelAdmin):
    search_fields = ["name", "description"]


@admin.register(Stream)
class StreamAdmin(ModelAdmin):
    search_fields = ["name", "description"]
