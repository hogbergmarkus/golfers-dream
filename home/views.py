from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactMessageForm


# Create your views here.
def index(request):
    """
    Renders the  home/index.html template.
    """
    return render(request, 'home/index.html')


def about(request):
    """
    Render the home/about.html template.
    """
    return render (request, 'home/about.html')


def contact(request):
    """
    Render the home/contact.html template,
    and the ContactMessageForm.
    """
    if request.method == "POST":
        contact_form = ContactMessageForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your message has been received!'
            )
            return redirect('home')

    contact_form = ContactMessageForm()

    return render(
        request,
        'home/contact.html',
        {
            'contact_form': contact_form
        },
    )
