from django.shortcuts import render
from .models import mockDb

def index(request):
    mock = mockDb.objects.all()
    return render(request, 'main/index.html', {"cities":mock})
