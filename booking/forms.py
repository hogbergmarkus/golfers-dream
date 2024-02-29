from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Form class for making a booking
    """
    class Meta:
        """
        Specifies the django model and order of the fields
        """
        model = Booking
        fields = (
            'first_name',
            'last_name',
            'email',
            'number_of_people',
            'check_in',
            'check_out',
            'message'
        )
