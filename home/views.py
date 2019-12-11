from django.shortcuts import render

def home(request):
    """ A view that displays the index page """
    return render(request, "home.html")
