from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from booking.models import Booking


# Create your views here.
@login_required
def user_profiles(request):
    """
    Render the user_profiles/user_profiles.html template.
    If user has made bookings, render them as well.

    """
    user_bookings = Booking.objects.filter(customer=request.user)

    return render(
        request,
        'user_profiles/user_profiles.html',
        {
            'bookings': user_bookings,
        }
    )
