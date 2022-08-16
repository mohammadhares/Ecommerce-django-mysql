from django import forms
from .models import *
from django import forms

class Admin_AccountForm(forms.ModelForm):
    class Meta:
        model = Admin_Account
        fields = "__all__"

class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"

class GalleriesForm(forms.ModelForm):
    class Meta:
        model = Galleries
        fields = "__all__"


class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = "__all__"

class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = "__all__"

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = "__all__"

class RefundsForm(forms.ModelForm):
    class Meta:
        model = Refunds
        fields = "__all__"
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"

class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = "__all__"
