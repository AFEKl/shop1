from django.shortcuts import render
from .models import *

# Create your views here.
def signin(request):
    return render(request, "core/sign-in.html")

def signup(request):
    return render(request, "core/sign-up.html")

def profile(request):
    profile = User.objects.all()
    return render(request, "core/profile.html", {"profile":profile})