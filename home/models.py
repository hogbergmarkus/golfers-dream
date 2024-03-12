from django.db import models


# Create your models here.
class ContactMessage(models.Model):
    """
    Model for contacting the resort
    """
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(blank=False)
    mark_as_read = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
