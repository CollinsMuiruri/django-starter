from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from .models import ParentOrGuardian, Student, Teacher  # Import your related models

User = get_user_model()

class EmailOrPhoneBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Try to fetch the user by email
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            # If email fails, try to fetch the user by phone number from related models
            user = None
            try:
                # Check ParentOrGuardian model
                parent = ParentOrGuardian.objects.get(phone_number=username)
                user = parent.user
            except ParentOrGuardian.DoesNotExist:
                try:
                    # Check Student model
                    student = Student.objects.get(phone_number=username)
                    user = student.user
                except Student.DoesNotExist:
                    try:
                        # Check Teacher model
                        teacher = Teacher.objects.get(phone_number=username)
                        user = teacher.user
                    except Teacher.DoesNotExist:
                        return None

        # Check the password
        if user and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None