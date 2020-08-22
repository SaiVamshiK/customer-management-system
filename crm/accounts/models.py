from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    phone=models.IntegerField(max_length=10, null=True)
    email=models.EmailField(max_length=200, null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    profile_pic = models.ImageField(default='default.jpg',null=True, blank=True)
    def __str__(self):
        return str(self.name)

class Tag(models.Model):
    name=models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.name)


class Product(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('OutDoor','OutDoor'),
    )
    name=models.CharField(max_length=200,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=200, null=True,choices=CATEGORY)
    description=models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags=models.ManyToManyField(Tag)
    def __str__(self):
        return str(self.name)

class Order(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Out for delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status=models.CharField(max_length=200,null=True,choices=STATUS)

    def __str__(self):
        return self.customer.name+','+self.product.name

