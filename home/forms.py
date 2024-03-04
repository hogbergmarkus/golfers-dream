from django import forms
from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    """
    Form class for contacting the resort.
    """
    class Meta:
        """
        Specifies the django model and order of the fields
        """
        model = ContactMessage
        fields = (
            'name',
            'email',
            'message',
        )
