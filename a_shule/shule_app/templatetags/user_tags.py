from django import template

register = template.Library()

@register.filter
def is_student(user):
    return hasattr(user, 'student_set')

@register.filter
def is_parent(user):
    return hasattr(user, 'parentorguardian_set')

@register.filter
def is_teacher(user):
    return hasattr(user, 'teacher_set')