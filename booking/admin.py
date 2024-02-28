from django.contrib import admin
from .models import Booking


# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Register the booking model in the admin panel.

    """
    list_display = (
        'customer',
        'first_name',
        'last_name',
        'email',
        'check_in',
        'status'
        )
    list_filter = (
        'status',
        'email',
        'check_in',
        'check_out',
        )
