from django.contrib.auth.base_user import BaseUserManager

# USER MANAGER
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password=None, commit=True, **extra_fields):
        # creates and saves a user with the given email and password
        if not email:
            raise ValueError("Users must have an email address!")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)

        if commit:
            user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password):
        # creates and saves a superuser with the given email and password
        user = self.create_user(password=password, email=email, commit=False)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
