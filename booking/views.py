from django.shortcuts import render
from django.contrib import messages
from .forms import BookingForm


# Create your views here.
def booking(request):
    """
    Render the booking/booking.html template,
    and the BookingForm.
    """
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Reservation received! Approval pending.'
            )
    
    booking_form = BookingForm()

    return render(
        request,
        'booking/booking.html',
        {
            'booking': booking,
            'booking_form': booking_form
        },
    )
