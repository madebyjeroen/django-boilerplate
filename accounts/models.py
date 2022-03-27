import uuid
from django.db import models
from django.utils import timezone
from accounts.managers import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

# USER MODEL
class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField("uuid", default=uuid.uuid4, unique=True, editable=False)
    email = models.EmailField(
        "email address",
        max_length=128,
        unique=True,
        error_messages={"unique": "A user with this email address already exists."},
    )
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text="Designates whether this user should be treated as active.",
    )
    is_staff = models.BooleanField(
        "staff",
        default=False,
        help_text="Designates whether the user can log into the admin site.",
    )
    created_date = models.DateTimeField(
        "created date", default=timezone.now, editable=False
    )
    updated_date = models.DateTimeField(
        "updated date", default=timezone.now, editable=False
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ("-created_date",)
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.updated_date = timezone.now()

        super().save(*args, **kwargs)
