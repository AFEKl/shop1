from django.shortcuts import render
from .models import *

# Create your views here.
def signin(request):
    return render(request, "core/sign-in.html")

def signup(request):
    if request.method == "POST":
        u_name = request.POST["username"]
        u_password = request.POST["password"]
        u_email = request.POST["email"]
        u_repassword = request.POST["repeat_password"]
        if u_password != u_repassword:
            return render(request, "core/sign-up.html",{'error':"пароли не совпадают"})
    return render(request, "core/sign-up.html")

def profile(request):

    return render(request, "core/profile.html")
