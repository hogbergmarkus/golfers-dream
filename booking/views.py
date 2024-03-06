from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import BookingForm
from .models import Booking


# Create your views here.
def booking(request):
    """
    Render the booking/booking.html template,
    and the BookingForm.
    """
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking_attempt = booking_form.save(commit=False)
            booking_attempt.customer = request.user
            booking_attempt.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Reservation received! Approval pending.'
            )
            return redirect('user_profiles')
        else:
            messages.add_message(
                request, messages.ERROR,
                'Something went wrong, please try agin.',
            )
            booking_form = BookingForm(data=request.POST)
            return render(
                request,
                'booking/booking.html',
                {'booking_form': booking_form}
            )

    booking_form = BookingForm()

    return render(
        request,
        'booking/booking.html',
        {
            'booking_form': booking_form
        },
    )


def edit_booking(request, booking_id):
    """
    View to edit bookings
    """
    booking = get_object_or_404(Booking, pk=booking_id)

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST, instance=booking)
        if booking_form.is_valid() and booking.customer == request.user:
            booking = booking_form.save(commit=False)
            booking.status = 'pending'
            booking.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Booking Updated!'
            )
            return redirect('user_profiles')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'There was an ERROR trying to update the booking.'
            )
    else:
        booking_form = BookingForm(instance=booking)

    return render(
        request,
        'booking/edit_booking.html',
        {
            'booking_form': booking_form
        },
    )


def delete_booking(request, booking_id):
    """
    View to delete bookings
    """
    booking = get_object_or_404(Booking, pk=booking_id)

    if request.method == "POST" and booking.customer == request.user:
        booking.delete()
        messages.success(
            request,
            'Booking has been deleted. We hope you will stay with us again!'
        )
        return redirect('user_profiles')
    else:
        return render(
            request,
            'booking/delete_booking.html',
            {
                'booking': booking
            },
        )
