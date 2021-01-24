from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def http404(request):
    return render(request, "404.html")


def http500(request):
    return render(request, "500.html")