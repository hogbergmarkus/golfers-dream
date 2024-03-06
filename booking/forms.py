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
        """
        Checks that check-in is not in the past
        """
        check_in = self.cleaned_data.get('check_in')
        if check_in < datetime.date.today():
            raise forms.ValidationError("Check-in date cannot be in the past.")
        return check_in

    def clean_check_out(self):
        """
        Checks that check-out is not in the past,
        and that check-out is not before check-in.
        """
        check_out = self.cleaned_data.get('check_out')
        check_in = self.cleaned_data.get('check_in')
        if check_out < datetime.date.today():
            raise forms.ValidationError(
                "Check-out date cannot be in the past."
                )

        if check_in and check_out < check_in:
            raise forms.ValidationError(
                'Check-out cannot be before check-in'
            )
        return check_out

    def clean_number_of_people(self):
        """
        Check that number of people is not less than 1,
        or higher than 10
        """
        number_of_people = self.cleaned_data.get('number_of_people')
        if number_of_people < 1 or number_of_people > 10:
            raise forms.ValidationError(
                "Number of people cannot be less than 1 or more than 10"
            )
        return number_of_people
