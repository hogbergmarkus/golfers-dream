from django.db import models
from django.contrib.auth.models import AbstractUser


USER_TYPES = (
    ('ST', 'Staff'),
    ('GU', 'Guest'),
)


# Create your models here.
class CustomUser(AbstractUser):
    """
    Add a custom user model
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    user_type = models.CharField(
        max_length=2, choices=USER_TYPES, default='GU'
        )
