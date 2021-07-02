from django.shortcuts import render
from .models import Soundcloud
# Create your views here.
def home(request):
    soundclouds = Soundcloud.objects
    return render(request, "home.html", {'soundclouds':soundclouds})
