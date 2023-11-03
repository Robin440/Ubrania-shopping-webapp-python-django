from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
from Customer.models import Customer


class Cart(models.Model):
    Cart_id = models.IntegerField(unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart ID: {self.Cart_id} - Customer: {self.customer.cus_name}"

class Product(models.Model):
    pname = models.CharField(max_length=255, default='Unknown')
    size = models.CharField(max_length=5, default='M')
    Qty = models.IntegerField(default=1, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, null=True, blank=True)
    section = models.ForeignKey('Section', on_delete=models.PROTECT)
    discount = models.IntegerField(default=0)
    price=models.IntegerField(null=True)
    prod_pic = models.ImageField(null=True,blank=True)
    prod_pic_two = models.ImageField(null=True,blank=True)
    prod_pic_three = models.ImageField(null=True,blank=True)
    small = models.CharField(null=True,blank=True)
    large = models.CharField(null=True, blank=True)
    xl = models.CharField(null=True,blank=True)
    xxl = models.CharField(null=True, blank=True)
    xxxl = models.CharField(null=True, blank=True)

    

    def __str__(self):
        return f"Product ID: {self.id} - Name: {self.pname}"

# class ProductImage(models.Model):
   
#     image = models.ImageField(null=True, blank=True,)




class Brand(models.Model):

    brand = models.CharField(max_length=255)
    
    discount = models.IntegerField(null=True)
    brand_img = models.ImageField(null=True,blank=True)

    def __str__(self):
        return f"Brand ID: {self.brand_id} - Name: {self.brand} - Section: {self.section.sectiontype}"

class Section(models.Model):
    
    sectiontype = models.CharField(max_length=255)
   
  
    discount = models.IntegerField(null=True,blank=True)
    section_img = models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return f"Section ID: {self.sectionid} - Type: {self.sectiontype} - Size: {self.size}"

class Order(models.Model):
    Order_id = models.IntegerField(unique=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"Order ID: {self.Order_id} - Cart ID: {self.cart.Cart_id} - Status: {self.status}"

class Wishlist(models.Model):
    Wish_id = models.IntegerField(unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return f"Wishlist ID: {self.Wish_id} - Customer: {self.customer.cus_name} - Product: {self.product.pname}"

class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    userreview = models.TextField()

    def __str__(self):
        return f"Review by {self.customer.cus_name} on {self.product.pname}"

class Profile(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    orders = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"Profile for {self.customer.cus_name}"
