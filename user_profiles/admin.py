from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """
    Customize the admin panel for displaying users.
    Add new fields to the Add user interface in Admin panel.
    """
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'user_type'
    )

    # Define the look of admin page when displaying users
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('User Type', {'fields': ('user_type',)}),

        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions'
            )}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Define fields of add user on admin page
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'first_name',
                'last_name',
                'username',
                'email',
                'password1',
                'password2'
                ),
        }),
    )

    search_fields = ('username', 'email')
    ordering = ('username',)


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
