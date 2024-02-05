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

    def __str__(self) -> str:
        return self.email

class TeamsChoices(models.IntegerChoices):
    ARSENAL = 0, 'Arsenal'
    ASTON_VILLA = 1, 'Aston Villa'
    BRENTFORD = 2, 'Brentford'
    BRIGHTON = 3, 'Brighton'
    BOURNEMOUTH = 4, 'Bournemouth'
    BURNLEY = 5, 'Burnley'
    CHELSEA = 6, 'Chelsea'
    CRYSTAL_PALACE = 7, 'Crystal Palace'
    EVERTON = 8, 'Everton'
    FULHAM = 9, 'Fulham'
    LIVERPOOL = 10, 'Liverpool'
    LUTON_TOWN = 11, 'Luton Town'
    MANCHESTER_CITY = 12, 'Manchester City'
    MANCHESTER_UNITED = 13, 'Manchester United'
    NEWCASTLE_UNITED = 14, 'Newcastle United'
    NOTTINGHAM_FOREST = 15, 'Nottingham Forset'
    SHEFFIELD_UNITED = 16, 'Sheffield United'
    TOTTENHAM_HOTSPUR = 17, 'Tottenham Hotspur'
    WESTHAM_UNITED = 18, 'Westham United'
    WOLVERHAMPTON_WANDERERS = 19, 'Wolverhamption Wanderers'

class UserProfile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=125, blank=True)
    last_name = models.CharField(max_length=125, blank=True)
    favorite_team = models.IntegerField(choices=TeamsChoices.choices, blank=True)
    cash = models.DecimalField(max_digits=6, decimal_places=2, default=0)