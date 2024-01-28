from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def trips(request):
    return render(request, 'trips.html')
