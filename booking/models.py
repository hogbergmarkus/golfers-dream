from django.db import models
from user_profiles.models import CustomUser


STATUS_TYPE = (
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('denied', 'Denied'),
)


# Create your models here.
class Booking(models.Model):
    """
    Stores a booking request related to CustomUser
    """
    customer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE
        )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    check_in = models.DateField()
    check_out = models.DateField()
    number_of_people = models.PositiveSmallIntegerField()
    message = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=15, choices=STATUS_TYPE, default='pending'
    )
