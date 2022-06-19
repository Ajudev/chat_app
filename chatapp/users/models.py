from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom User model which extends from the BaseUser Model of Django
    """
    gender_choice = [("M", "Male"), ("F", "Female"), ("O", "Others")]
    user_type_choice = [("app", "App"), ("dashboard", "Dashboard"), ("admin", "Admin")]

    username = None
    email = models.EmailField(
        verbose_name='Email Address', max_length=255, unique=True, db_index=True)
    gender = models.CharField(choices=gender_choice,
                              max_length=10, blank=True, null=True)
    user_type = models.CharField(choices=user_type_choice,
                                 verbose_name="User type for permissions", max_length=255, default="app")
    profile_img = models.ImageField(
        upload_to="profile", verbose_name="Profile image", blank=True, null=True)

    USERNAME_FIELD = 'email'

    class Meta:
        """
        Meta data for User model
        """
        permissions = [
            ('app_user', 'App User Permissions'),  # usage: 'users.app_user'
            # usage: 'users.dashboard_user'
            ('dashboard_user', 'Dashboard User Permissions'),
            ('admin_user', 'Dashboard User Permissions'),
        ]
        db_table = 'chat_users'

    def __str__(self) -> str:
        return self.email
    