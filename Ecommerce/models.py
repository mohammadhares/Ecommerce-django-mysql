from django.forms import ModelForm, Textarea, ImageField
from django.db import models

class Admin_Account(models.Model):
    id = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=100)
    Email = models.EmailField(max_length=200,unique=True)
    Password = models.CharField(max_length=200)
    Permission = models.IntegerField()
    Status = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'Admin_Account'

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    seller_id = models.CharField(max_length=200, default=0)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'Categories'

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    categories_id = models.ForeignKey(
        "Categories", on_delete=models.CASCADE)
    seller_id = models.CharField(max_length=200, default=0)
    Product_Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=500)
    Price = models.CharField(max_length=200)
    Quantity = models.BigIntegerField()
    Stock = models.CharField(max_length=200)
    Image = models.ImageField(upload_to="media/Products/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'Products'

class Galleries(models.Model):
    id = models.AutoField(primary_key=True)
    Products_id = models.ForeignKey(
        "Products", on_delete=models.CASCADE)
    Image = models.ImageField(upload_to="media/Galleries/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'Galleries'

class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    Phone = models.CharField(max_length=200)
    Email = models.CharField(max_length=200,unique=True)
    Address = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    Image = models.ImageField(upload_to="media/Customers/")
    Payment_Type = models.CharField(max_length=200)
    Card_no = models.CharField(max_length=200)
    Card_cvs = models.CharField(max_length=200)
    Card_exp = models.CharField(max_length=200)
    PaymentPhone = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'Customers'

class Shipping(models.Model):
    id = models.AutoField(primary_key=True)
    Shipping_Type = models.CharField(max_length=200)
    Shipping_Zone = models.CharField(max_length=200)
    Price = models.BigIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'Customers'

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    Customers_id = models.ForeignKey(
        "Customers", on_delete=models.CASCADE)
    Products_id = models.ForeignKey(
        "Products", on_delete=models.CASCADE)
    Status = models.CharField(max_length=200)
    Message = models.CharField(max_length=500)
    Shipping_id = models.ForeignKey(
        "Shipping", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'Orders'

class Refunds(models.Model):
    id = models.AutoField(primary_key=True)
    Customers_id = models.ForeignKey(
        "Customers", on_delete=models.CASCADE)
    Products_id = models.ForeignKey(
        "Products", on_delete=models.CASCADE)
    Reason = models.CharField(max_length=200)
    Request_Status = models.CharField(max_length=500)
    Refund_Status = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'Refunds'

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=500)
    Image = models.ImageField(upload_to="media/Blogs/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'Blog'

class Contacts(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Subject = models.CharField(max_length=200)
    Message = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'Contacts'


class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'Seller'

