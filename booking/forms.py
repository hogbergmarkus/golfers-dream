from django import forms
from .models import Booking
import datetime


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
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_check_in(self):
        check_in = self.cleaned_data['check_in']
        if check_in < datetime.date.today():
            raise forms.ValidationError("Check-in date cannot be in the past.")
        return check_in

    def clean_check_out(self):
        check_out = self.cleaned_data['check_out']
        if check_out < datetime.date.today():
            raise forms.ValidationError(
                "Check-out date cannot be in the past or before Check-in"
                )
        return check_out
