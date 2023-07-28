from django.shortcuts import render

from .models import Cities, Weather

def index(request):

    cities = Cities.objects.values()
    weather = Weather.objects.values()
    selected_city = request.POST.get('select_city', False)
    print(selected_city)

    return render(request, 'main/index.html', {"cities":cities, "weather": weather})
