from django.shortcuts import render

from .forms import WeatherForm

def index(request):

    cities = WeatherForm();

    return render(request, 'main/index.html', {"cities":cities})
