from django.shortcuts import render

# Create your views here.
def user_profiles(request):
    """
    Render the user_profiles/user_profiles.html template.
    """
    return render (request, 'user_profiles/user_profiles.html')
