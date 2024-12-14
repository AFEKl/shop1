from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from shop.models import *


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

def create_product(request):
    if request.method == "POST":
        p_name = request.POST["name"]
        p_description = request.POST["description"]
        p_price = request.POST["price"]
        p_discount = request.POST["discount"]
        p_count = request.POST["count"]
        p_tip = request.POST["tip"]
        p_garanty = request.POST["garanty"]
        p_publisher = request.POST["publisher"]
        p_image = request.POST["image"]
        p_rating = request.POST["rating"]
        Product.objects.create(
            title=p_name,
            description=p_description,
            prise=p_price,
            discount=p_discount,
            count=p_count,
            tip=p_tip,
            Garanty=p_garanty,
            publisher=p_publisher,
            image = p_image,
            rating = p_rating,
        )
        return redirect("main")

    return render(request, "core/create_product.html")
