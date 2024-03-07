from django import forms
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    """
    Extends the allauth signup form with additional fields.
    """
    first_name = forms.CharField(
        max_length=50, required=True, label='First Name'
        )
    last_name = forms.CharField(
        max_length=50, required=True, label='Last Name'
        )
    username = forms.CharField(max_length=50, required=True, label='Username')
    email = forms.EmailField(max_length=50, required=True, label='Email')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']

        user.save()
        return user
