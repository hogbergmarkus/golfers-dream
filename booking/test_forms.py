from django.test import TestCase
from .forms import BookingForm


# Create your tests here.
class TestBookingForm(TestCase):
    """
    Tests for BookingForm
    """
    def test_booking_form_is_valid(self):
        """
        Test for all fields
        """
        booking_form = BookingForm({
            'first_name': 'Computer',
            'last_name': 'Wiz',
            'email': 'test.test@test.org',
            'number_of_people': 2,
            'check_in': '2050-04-01',
            'check_out': '2050-04-04',
            'message': 'Just testing',
        })
        self.assertTrue(booking_form.is_valid(), msg='Form not valid')

    def test_first_name_is_required(self):
        """
        Test for first_name field
        """
        booking_form = BookingForm({
            'first_name': '',
            'last_name': 'Wiz',
            'email': 'test.test@test.org',
            'number_of_people': 2,
            'check_in': '2050-04-01',
            'check_out': '2050-04-04',
            'message': 'Just testing',
        })
        self.assertFalse(
            booking_form.is_valid(),
            msg='First name empty, but form is valid'
            )

    def test_last_name_is_required(self):
        """
        Test for last_name field
        """
        booking_form = BookingForm({
            'first_name': 'Computer',
            'last_name': '',
            'email': 'test.test@test.org',
            'number_of_people': 2,
            'check_in': '2050-04-01',
            'check_out': '2050-04-04',
            'message': 'Just testing',
        })
        self.assertFalse(
            booking_form.is_valid(),
            msg='Last name empty, but form is valid'
            )

    def test_email_is_required(self):
        """
        Test for email field
        """
        booking_form = BookingForm({
            'first_name': 'Computer',
            'last_name': 'Wiz',
            'email': '',
            'number_of_people': 2,
            'check_in': '2050-04-01',
            'check_out': '2050-04-04',
            'message': 'Just testing',
        })
        self.assertFalse(
            booking_form.is_valid(),
            msg='Email field empty, but form is valid'
            )

    def test_email_field_is_invalid(self):
        """
        Test for email field invalid
        """
        booking_form = BookingForm({
            'first_name': 'Computer',
            'last_name': 'Wiz',
            'email': 'test.test.org',
            'number_of_people': 2,
            'check_in': '2050-04-01',
            'check_out': '2050-04-04',
            'message': 'Just testing',
        })
        self.assertFalse(
            booking_form.is_valid(),
            msg='Email field invalid, but form is valid'
            )

    def test_number_of_people_is_required(self):
        """
        Test for number_of_people field
        """
        booking_form = BookingForm({
            'first_name': 'Computer',
            'last_name': 'Wiz',
            'email': 'test.test@test.org',
            'number_of_people': None,
            'check_in': '2050-04-01',
            'check_out': '2050-04-04',
            'message': 'Just testing',
        })
        self.assertFalse(
            booking_form.is_valid(),
            msg='Number of people field empty, but form is valid'
            )

    def test_check_in_is_required(self):
        """
        Test for check_in field
        """
        booking_form = BookingForm({
            'first_name': 'Computer',
            'last_name': 'Wiz',
            'email': 'test.test@test.org',
            'number_of_people': 2,
            'check_in': '',
            'check_out': '2050-04-04',
            'message': 'Just testing',
        })
        self.assertFalse(
            booking_form.is_valid(),
            msg='Check in field empty, but form is valid'
            )

    def test_check_in_is_invalid(self):
        """
        Test for check_in field valid
        """
        booking_form = BookingForm({
            'first_name': 'Computer',
            'last_name': 'Wiz',
            'email': 'test.test@test.org',
            'number_of_people': 2,
            'check_in': '2050-04-0',
            'check_out': '2050-04-04',
            'message': 'Just testing',
        })
        self.assertFalse(
            booking_form.is_valid(),
            msg='Check in field invalid, but form is valid'
            )

    def test_check_out_is_required(self):
        """
        Test for check_out field
        """
        booking_form = BookingForm({
            'first_name': 'Computer',
            'last_name': 'Wiz',
            'email': 'test.test@test.org',
            'number_of_people': 2,
            'check_in': '2050-04-01',
            'check_out': '',
            'message': 'Just testing',
        })
        self.assertFalse(
            booking_form.is_valid(),
            msg='Check out field empty, but form is valid'
            )

    def test_check_out_is_invalid(self):
        """
        Test for check_out field valid
        """
        booking_form = BookingForm({
            'first_name': 'Computer',
            'last_name': 'Wiz',
            'email': 'test.test@test.org',
            'number_of_people': 2,
            'check_in': '2050-04-01',
            'check_out': '2050-04-0',
            'message': 'Just testing',
        })
        self.assertFalse(
            booking_form.is_valid(),
            msg='Check out field invalid, but form is valid'
            )

    def test_message_is_valid(self):
        """
        Test for message field is valid
        """
        booking_form = BookingForm({
            'first_name': 'Computer',
            'last_name': 'Wiz',
            'email': 'test.test@test.org',
            'number_of_people': 2,
            'check_in': '2050-04-01',
            'check_out': '2050-04-04',
            'message': '',
        })
        self.assertTrue(
            booking_form.is_valid(),
            msg='Form not valid'
            )

    def test_check_out_before_check_in_is_invalid(self):
        """
        Test for check_out before check-in invalid
        """
        booking_form = BookingForm({
            'first_name': 'Computer',
            'last_name': 'Wiz',
            'email': 'test.test@test.org',
            'number_of_people': 2,
            'check_in': '2050-04-20',
            'check_out': '2024-04-19',
            'message': 'Just testing',
        })
        self.assertFalse(
            booking_form.is_valid(),
            msg='Check out before check-in, but form is valid'
            )

    def test_check_in_before_today_date(self):
        """
        Test for check_in before today date
        """
        booking_form = BookingForm({
            'first_name': 'Computer',
            'last_name': 'Wiz',
            'email': 'test.test@test.org',
            'number_of_people': 2,
            'check_in': '2024-03-04',
            'check_out': '2050-03-11',
            'message': 'Just testing',
        })
        self.assertFalse(
            booking_form.is_valid(),
            msg='Check in before today date, but form is valid'
            )

    def test_number_of_people_not_zero(self):
        """
        Test for number of people not to be 0
        """
        booking_form = BookingForm({
            'first_name': 'Computer',
            'last_name': 'Wiz',
            'email': 'test.test@test.org',
            'number_of_people': 0,
            'check_in': '2050-03-04',
            'check_out': '2050-03-11',
            'message': 'Just testing',
        })
        self.assertFalse(
            booking_form.is_valid(),
            msg='Number of people is 0'
            )
