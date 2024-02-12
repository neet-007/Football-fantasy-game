from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('user must provide an email')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)

        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True

        user.save()
        return user

class UserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=125, unique=True)
    username = None

    objects = UserManager()

    USERNAME_FIELD = 'email'

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.email

