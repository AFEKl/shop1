from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *


def signin(request):
    if request.method == "POST":
        u_name = request.POST["username"]
        u_password = request.POST["password"]
        user = authenticate(request, username=u_name, password=u_password)
        if user is not None:
            login(request, user)
            return redirect("main")
        else:
            return render(request, "core/sign-in.html", {'error':"неверное имя пользователя или пароль"})
    return render(request, "core/sign-in.html")

def signup(request):
    if request.method == "POST":
        u_name = request.POST["username"]
        u_password = request.POST["password"]
        u_email = request.POST["email"]
        u_repassword = request.POST["repeat_password"]
        if u_password != u_repassword:
            return render(request, "core/sign-up.html",{'error':"пароли не совпадают"})
        User.objects.create_user(
            username=u_name,
            password=u_password,
            email=u_email,
        )
        return redirect("signin")

        
    return render(request, "core/sign-up.html")
def sign_out(request):
    logout(request)
    return redirect("signin")

def profile(request):

    return render(request, "core/profile.html")
