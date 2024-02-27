from django.shortcuts import render


# Create your views here.
def index(request):
    """
    Renders the  home/index.html template.
    """
    return render(request, 'home/index.html')
