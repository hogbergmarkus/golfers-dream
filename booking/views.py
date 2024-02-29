from django.shortcuts import render
from django.contrib import messages
from .forms import BookingForm
from .models import Booking


# Create your views here.
def booking(request):
    """
    Render the booking/booking.html template.
    """
    return render(request, 'booking/booking.html')
