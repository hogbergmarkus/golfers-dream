from django.contrib import admin
from .models import ContactMessage


# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'created_on',
        'mark_as_read',
        )
    list_filter = (
        'email',
        'mark_as_read',
        )
