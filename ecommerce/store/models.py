from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(user,on_delete=models.CASECADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=200,null=True)
    price=models.FloatField()
    digital=models.BooleanField(default=False,null=False,blank=False)
    #image=
    def __str__(self):
        return self.name


class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.Set_Null,blank=True,null=True)
    date_orderd=models.DateTimeField(auto_new_add=True)
    complete=models.BooleanField(default=False,null=False,blank=False)
    transaction_id=modles.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.Set_Null,blank=True,null=True)
    order=models.ForeignKey(Order,on_delete=models.Set_Null,blank=True,null=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(auto_new_add=True)

class ShippingAdderss(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.Set_Null,blank=True,null=True)



