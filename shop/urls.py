from django.urls import path
from shop.views import *


urlpatterns = [
    path('', catalog, name="main"),
    path('orders/', orders, name="orders"),
    path('create/<int:product_id>/', create, name="order_create"),
    path('detail/<int:product_id>/', detail, name="product_detail"),
]