from django.shortcuts import render

def home_view(request):
    """ A view that displays the index page """
    return render(request, "index.html")
