from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from .models import Teacher, Student, ParentOrGuardian

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin


# Register your models here.
admin.site.unregister(User)
admin.site.unregister(Group)


# @admin.register(User,UserAdmin)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    # Add search fields for username and email
    search_fields = ["username", "email"]


admin.site.register(User, UserAdmin)


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(ModelAdmin):
    # Add the 'user' field to autocomplete_fields
    autocomplete_fields = ["user"]
    search_fields = ["teacher_id", "email", "f_name", "l_name"]    
    list_display = ['teacher_id', 'f_name', 'l_name', 'email', 'join_date']


@admin.register(Student)
class StudentAdmin(ModelAdmin):
    # Add the 'user' field to autocomplete_fields
    autocomplete_fields = ["user"]
    search_fields = ["student_id", "email", "f_name", "l_name"]    
    list_display = ['student_id', 'f_name', 'l_name', 'email', 'join_date']
    autocomplete_fields = ["class_grade"]

@admin.register(ParentOrGuardian)
class ParentOrGuardianAdmin(ModelAdmin):
    # Add the 'user' field to autocomplete_fields
    autocomplete_fields = ["user", "child"]
    search_fields = ["parent_id", "email", "f_name", "l_name"]    
    list_display = ['f_name', 'l_name', 'email', 'child', 'relation']
