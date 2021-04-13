from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from .manager import CustomManager


# Create your models here.
class UserTable(AbstractUser):
    """User Model for Customized User."""
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, null=False, blank=False,
                                validators=[RegexValidator(r'[A-Za-z0-9@#$%^&+=]{8,}',
                                                           message='Must have atleast one: A-Z,a-z,0-9,sp. character')])
    first_name = None
    last_name = None
    firstName = models.CharField(max_length=150, blank=True)
    lastName = models.CharField(max_length=150, blank=True)
    player_name = models.CharField(max_length=150)
    user_id = models.PositiveBigIntegerField(unique=True, blank=False, null=True)
    team_name = models.CharField(max_length=150, unique=True, blank=False, null=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomManager()

    def __str__(self):
        return str(self.first_name)

