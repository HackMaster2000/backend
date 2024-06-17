from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', default='products/sin-producto.jpg')
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.name

class Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    rating=models.IntegerField(null=True,blank=True,default=0)
    comment=models.TextField(null=True,blank=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return str(self.rating)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    publish_date = models.DateField()
    image = models.ImageField(upload_to='blog_images/')
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    author_name = models.CharField(max_length=100)
    author_position = models.CharField(max_length=100)
    author_company = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonial_images/')
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.author_name

class TeamMember(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='team_images/')
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.email

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    paymentMethod=models.CharField(max_length=200,null=True,blank=True)
    taxPrice=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    shippingPrice=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    totalPrice=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    isPaid=models.BooleanField(default=False)
    paidAt=models.DateTimeField(auto_now_add=False,null=True,blank=True)
    isDelivered=models.BooleanField(default=False)
    deliveredAt=models.DateTimeField(auto_now_add=False,null=True,blank=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)
    
    
    def __str__(self):
        return str(self.createdAt)


class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    qty=models.IntegerField(null=True,blank=True,default=0)
    price=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    image=models.CharField(max_length=200,null=True,blank=True)
    _id=models.AutoField(primary_key=True,editable=False)

        
    def __str__(self):
        return self.name

class ShippingAddress(models.Model):
    order=models.OneToOneField(Order,on_delete=models.CASCADE,null=True,blank=True)
    address=models.CharField(max_length=200,null=True,blank=True)
    city=models.CharField(max_length=200,null=True,blank=True)
    postalCode=models.CharField(max_length=200,null=True,blank=True)
    country=models.CharField(max_length=200,null=True,blank=True)
    shippingPrice=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.address