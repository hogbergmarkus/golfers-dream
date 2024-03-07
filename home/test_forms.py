from django.test import TestCase
from .forms import ContactMessageForm


# Create your tests here.
class TestContactMessageForm(TestCase):
    """
    Tests for ContactMessageForm
    """

    def test_form_is_valid(self):
        """
        Test for all fields
        """
        contact_form = ContactMessageForm({
            'name': 'Computer wiz',
            'email': 'test.test@test.org',
            'message': 'Hello, room for two please.',
        })
        self.assertTrue(contact_form.is_valid(), msg='Form not valid')

    def test_name_is_reqiured(self):
        """
        Test for name field
        """
        contact_form = ContactMessageForm({
            'name': '',
            'email': 'test.test@test.org',
            'message': 'Hello, room for two please.',
        })
        self.assertFalse(
            contact_form.is_valid(),
            msg='Name was not provided, but form is valid'
            )

    def test_email_is_reqiured(self):
        """
        Test for email field
        """
        contact_form = ContactMessageForm({
            'name': 'Computer wiz',
            'email': '',
            'message': 'Hello, room for two please.',
        })
        self.assertFalse(
            contact_form.is_valid(),
            msg='Email was not provided, but form is valid'
            )

    def test_message_is_reqiured(self):
        """
        Test for message field
        """
        contact_form = ContactMessageForm({
            'name': 'Computer wiz',
            'email': 'test.test@test.org',
            'message': '',
        })
        self.assertFalse(
            contact_form.is_valid(),
            msg='Message was not provided, but form is valid'
            )

    def test_email_is_email_address(self):
        """
        Test for invalid email field
        """
        contact_form = ContactMessageForm({
            'name': 'Computer wiz',
            'email': 'test.test.test.org',
            'message': 'Hello, room for two please.',
        })
        self.assertFalse(
            contact_form.is_valid(),
            msg='Email was not provided correctly, but form is valid'
            )
