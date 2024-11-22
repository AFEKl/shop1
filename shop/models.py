from django.db import models


class Product(models.Model) :
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="static/shop/img/")
    prise = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    rating = models.PositiveSmallIntegerField()
    discount = models.PositiveIntegerField()
    publisher = models.CharField(max_length=50,)
    tip = models.CharField(max_length=50,)
    Garanty = models.CharField(max_length=50)

class Order(models.Model) :
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    address = models.TextField()
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=254)
    comment = models.TextField(blank=True, null=True)
    count = models.PositiveIntegerField(default=1)
