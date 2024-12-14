from django.shortcuts import render
from .models import *

def catalog(request):
    products = Product.objects.all()
    return render(request, "shop/catalog.html", {"products": products})


def orders(request):
    orders = Order.objects.all()
    return render(request, "shop/orders.html", {"orders":orders})


def create(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        if request.user.is_authenticated:
            u_address = request.POST["address"]
            u_email = request.POST["email"]
            u_phone = request.POST["phone"]
            u_count = int(request.POST["count"])
            u_comment = request.POST["comment"]
            Order.objects.create(
                product = product,
                address = u_address,
                phone = u_phone,
                email = u_email,
                comment = u_comment,
                count = u_count
            )
        else:
            return render(request, "shop/create_order.html",{'error':"Вы не авторизованы! Пожалуйста, авторизуйтесь."})
    return render(request, "shop/create_order.html", {"success": "Заказ успешно создан!"})


def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "shop/product_detail.html", {"id_product": product})



