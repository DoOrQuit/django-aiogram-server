import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("Please, provide a correct email.")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if not kwargs.get('is_staff'):
            raise ValueError("Superuser must have 'is_staff' value set to True")

        if not kwargs.get('is_superuser'):
            raise ValueError("Superuser must have 'is_superuser' value set to True")

        if not kwargs.get('is_active'):
            raise ValueError("Superuser must have 'is_active' value set to True")
        return self.create_user(email, password, **kwargs)


class User(AbstractBaseUser):

    """ Custom user model """

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128, null=True)
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return f"[{self.id}]{self.email}"




