from cmath import inf
from os import stat
from unicodedata import category
from django.shortcuts import render, redirect
from requests.sessions import session
from sqlalchemy import null
from stripe import Product
from .models import *
from django.contrib import messages
from django.db.models import Count, Sum


def Admin_login_required(function):
    def wrapper(request, *args, **kw):
        user = request.user
        if not (request.session.get('AdminEmail')):
            return redirect('Dashboard_Login')
        else:
            return function(request, *args, **kw)
    return wrapper

def Customer_login_required(function):
    def wrapper(request, *args, **kw):
        user = request.user
        if not (request.session.get('CustomerID')):
            return redirect('Account')
        else:
            return function(request, *args, **kw)
    return wrapper
    

def home(request):
    productsList = Products.objects.all()
    NewProductsList = Products.objects.all().reverse()[:9]
    productinfo = Products.objects.all()
    populerProduct = Products.objects.all().order_by('?')
    info = Blog.objects.all()
    if not (request.session.get('CustomerID')):
        basketCount = 0
        return render(request, "home/index.html", {'populerProduct':populerProduct, 'NewProductsList':NewProductsList, 'productsList': productsList, 'basketCount': basketCount,  'info': info})
    else:
        customerID = request.session['CustomerID']
        basketCount = Orders.objects.filter(
            Customers_id_id=customerID, Status='On Hold').count()
        orderinfo = Orders.objects.filter(
            Customers_id_id=customerID, Status='On Hold')
        ShippingInfo = Shipping.objects.all()
        customerInfo = Customers.objects.filter(id=customerID)
        OrderHistory = Orders.objects.raw('SELECT ecommerce_orders.Products_id_id, ecommerce_products.id,  sum(ecommerce_products.Price) as price from ecommerce_orders INNER join ecommerce_products on ecommerce_orders.Products_id_id = ecommerce_products.id where ecommerce_orders.Customers_id_id = "'+str(
            customerID)+'" and ecommerce_orders.Status="On Hold"')

        return render(request, "home/index.html", {'populerProduct':populerProduct, 'NewProductsList':NewProductsList, 'OrderHistory': OrderHistory, 'productsList': productsList, 'basketCount': basketCount, 'productinfo': productinfo, 'orderinfo': orderinfo, 'ShippingInfo': ShippingInfo, 'customerInfo': customerInfo, 'info': info})

def Shop(request):
    productsList = Products.objects.all()
    category = Categories.objects.all()
    return render(request,"home/Shop.html",{'productsList':productsList,'category':category})

def SearchCategory(request, id):
    productsList = Products.objects.filter(categories_id_id=id)
    category = Categories.objects.all()
    return render(request,"home/Shop.html",{'productsList':productsList,'category':category})


def Account(request):
    return render(request, "home/login.html")

def About(request):
    return render(request, 'home/about.html')


@Admin_login_required
def Dashboard(request):
    productt = Products.objects.all().count()
    Customer = Customers.objects.all().count()
    Order = Orders.objects.all().count()
    Contact = Contacts.objects.all().count()
    blog = Blog.objects.all().count()
    AdminAccount = Admin_Account.objects.all().count()
    Gallery = Galleries.objects.all().count()

    return render(request, "Dashboard/index.html",{'Gallery':Gallery, 'AdminAccount':AdminAccount, 'blog':blog, 'productt':productt,'Customer':Customer,'Order':Order,'Contact':Contact})


def Dashboard_Login(request):
    return render(request, "Dashboard/login.html")


def Dashboard_Logout(request):
    del request.session['AdminEmail']
    del request.session['Permission']
    del request.session['LoginName']
    del request.session['admin_id']
    return redirect('Dashboard_Login')


def Admin_Login(request):
    if request.method == "POST":
        Email = request.POST['Email']
        Password = request.POST['Password']
        if Email == "":
            messages.error(request, "Please Enter Email")
            return redirect('Dashboard_Login')
        elif Password == "":
            messages.error(request, "Please Enter Password")
            return redirect('Dashboard_Login')
        else:
            if Admin_Account.objects.filter(Email=Email).exists():
                Info = Admin_Account.objects.get(Email=Email)
                password = Info.Password
                if password == Password:
                    request.session['AdminEmail'] = Email
                    request.session['admin_id'] = Info.id
                    request.session['Permission'] = Info.Permission
                    request.session['LoginName'] = Info.Username
                    Admin_Account.objects.filter(
                        Email=Email).update(Status='Online')
                    messages.success(request, "Welcome")
                    return redirect('Dashboard')
                else:
                    messages.error(request, "Incorrect Username or Password")
                    return redirect('Dashboard_Login')
            else:
                messages.error(request, "Incorrect Email")
                return redirect('Dashboard_Login')
    else:
        return redirect('Dashboard_Login')


@Admin_login_required
def AdminAccounts(request):
    AdminAccount = Admin_Account.objects.all().reverse()
    return render(request, "Dashboard/AdminAccounts.html", {'AdminAccount': AdminAccount})


def RegisterAccount(request):
    if request.method == "POST":
        if request.POST.get('AccountNo', False) == 0:
            AccountNo = '0'
        else:
            AccountNo = request.POST['AccountNo']

        if request.POST.get('CVC', False) == 0:
            CVC = '0'
        else:
            CVC = request.POST['CVC']

        if request.POST.get('ExpireDate', False) == 0:
            ExpireDate = '0'
        else:
            ExpireDate = request.POST['ExpireDate']

        if request.POST.get('PaymentPhone', False) == 0:
            Payment_Phone = '0'
        else:
            Payment_Phone = request.POST['PaymentPhone']

        Customer = Customers(FirstName=request.POST['firstName'], LastName=request.POST['lastName'], Phone=request.POST['Phone'], Email=request.POST['Email'], Password=request.POST['Password'],
                             Image=request.FILES['image'], Payment_Type=request.POST['PaymentMethod'], Address=request.POST['Address'], Card_no=AccountNo, Card_cvs=CVC, Card_exp=ExpireDate, PaymentPhone=Payment_Phone)
        Customer.save()
        messages.success(request, "Saved")
        return redirect('Account')
    else:
        return redirect('Account')


@Admin_login_required
def CustomersAccounts(request):
    Customer = Customers.objects.all().reverse()
    return render(request, "Dashboard/CustomerAccount.html", {'Customer': Customer})


def CustomerLogin(request):
    if request.method == "POST":
        Email = request.POST['Email']
        Password = request.POST['Password']
        if Email == "":
            messages.error(request, "Please Enter Email")
            return redirect('Account')
        elif Password == "":
            messages.error(request, "Please Enter Password")
            return redirect('Account')
        else:
            if Customers.objects.filter(Email=Email).exists():
                Info = Customers.objects.get(Email=Email)
                password = Info.Password
                if password == Password:
                    request.session['CustomerAddress'] = Info.Address
                    request.session['CustomerName'] = Info.FirstName
                    request.session['CustomerID'] = Info.id
                    messages.success(request, "Welcome")
                    return redirect('home')
                else:
                    messages.error(request, "Incorrect Username or Password")
                    return redirect('Account')
            else:
                messages.error(request, "Incorrect Email")
                return redirect('Account')
    else:
        return redirect('Account')

@Admin_login_required
def AllProducts(request):
    Categories_ = Categories.objects.all().reverse()
    Products_ = Products.objects.all().reverse()
    Gallery = Galleries.objects.all()
    return render(request, "Dashboard/Products.html", {'Categories_': Categories_, 'Products_': Products_, 'Gallery': Gallery})


def AddCategory(request):
    if request.method == "POST":
        seller_id = 0
        if(request.session['seller_id']):
            seller_id = request.session['seller_id']
        
        saveCategory = Categories(name=request.POST['CategoryName'], seller_id= seller_id)
        saveCategory.save()
        messages.success(request, "Category Added")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))

def AddProduct(request):
    if request.method == "POST":
        seller_id = 0
        if(request.session['seller_id']):
            seller_id = request.session['seller_id']
        
        saveProduct = Products(seller_id=seller_id, Product_Name=request.POST['ProductName'], Description=request.POST['Description'], Price=request.POST['Price'],
                               Quantity=request.POST['Quantity'], Stock=request.POST['InStock'], categories_id_id=request.POST['CategoryID'], Image=request.FILES['Image'])
        saveProduct.save()
        messages.success(request, "Product Added")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))



def Products_details(request, id):
    product_info = Products.objects.filter(id=id)
    product_Category = Products.objects.get(id=id)
    galleryInfo = Galleries.objects.filter(Products_id_id=id)
    categInfo = Categories.objects.get(id=product_Category.categories_id_id)
    return render(request, "home/Products_details.html", {'product_info': product_info, 'categInfo': categInfo.name, 'galleryInfo': galleryInfo})

def UploadGallery(request):
    if request.method == "POST":
        files = request.FILES.getlist('Images')
        for f in files:
            result = Galleries(
                Image=f, Products_id_id=request.POST['ProductID'])
            result.save()
        messages.success(request, "Gallery Uploaded")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, "Error")
        return redirect(request.META.get('HTTP_REFERER'))

@Customer_login_required
def AddOrders(request, productID):
    if request.method == "POST":
        result = Orders(Products_id_id=productID, Message=request.POST['DeliveryNote'],Status='On Hold', Customers_id_id=request.session['CustomerID'], Shipping_id_id='1')
        result.save()
        messages.success(request, "Order Saved")
        return redirect('home')

@Customer_login_required
def AddOrder(request):
    if request.method == "POST":
        customerID = request.session['CustomerID']
        result = Orders.objects.filter(Customers_id_id=customerID, Status='On Hold').update(
            Status='On Hold', Shipping_id_id=request.POST['ShippmentID'])
        messages.success(request, "Paid Successfully")
        return redirect('home')


@Customer_login_required
def CustomerAccount(request):
    productsList = Products.objects.all()
    shipmentList = Shipping.objects.all()
    RefundsInfo = Refunds.objects.all()
    customerID = request.session['CustomerID']
    customerInfo = Customers.objects.filter(id=customerID)
    result = Orders.objects.filter(
        Customers_id_id=customerID).select_related('Products_id')
    return render(request, "home/Account.html", {'customerInfo': customerInfo, 'RefundsInfo': RefundsInfo, 'OrderInfo': result, 'productsList': productsList, 'shipmentList': shipmentList})

@Customer_login_required
def CancelOrder(request, id):
    return render(request, "home/CancelOrder.html", {'productID': id})


@Customer_login_required
def CancelRequest(request, id):
    if request.method == "POST":
        customerID = request.session['CustomerID']
        result = Refunds(Reason=request.POST['Reason'], Request_Status='Pending',
                         Refund_Status='Pending', Customers_id_id=customerID, Products_id_id=id)
        result.save()
        Orders.objects.filter(Products_id_id=id).update(Status='Cancel')
        messages.success(request, "Requested")
        return redirect('CustomerAccount')

@Admin_login_required
def AdminOrders(request):
    productsList = Products.objects.all()
    shipmentList = Shipping.objects.all()
    RefundsInfo = Refunds.objects.all()
    Customer = Customers.objects.all()

    result = Orders.objects.all().select_related('Products_id')
    return render(request, "Dashboard/AdminOrders.html", {'Customer':Customer, 'OrderInfo': result, 'shipmentList': shipmentList, 'productsList': productsList, 'RefundsInfo': RefundsInfo})

def Change_Refund_Status(request, status, id):
    if status == 'Accept':
        Refunds.objects.filter(Products_id_id=id).update(
            Request_Status='Accepted', Refund_Status='Accepted')
        messages.success(request, "Accepted")
        return redirect('AdminOrders')
    else:
        Refunds.objects.filter(Products_id_id=id).update(
            Request_Status='Rejected', Refund_Status='Rejected')
        messages.success(request, "Rejected")
        return redirect('AdminOrders')


def Customerlogout(request):
    del request.session['CustomerName']
    del request.session['CustomerID']
    return redirect('home')


@Customer_login_required
def UpdateCustomer(request):
    if request.method == "POST":
        customerID = request.session['CustomerID']
        cinfo = Customers.objects.get(id=customerID)
        
        if request.POST.get('AccountNo', False) == 0:
            AccountNo = cinfo.Card_no
        else:
            AccountNo = request.POST['AccountNo']

        if request.POST.get('CVC', False) == 0:
            CVC = cinfo.Card_cvs
        else:
            CVC = request.POST['CVC']

        if request.POST.get('ExpireDate', False) == 0:
            ExpireDate = cinfo.Card_exp
        else:
            ExpireDate = request.POST['ExpireDate']

        if request.POST.get('PaymentPhone', False) == 0:
            Payment_Phone = cinfo.PaymentPhone
        else:
            Payment_Phone = request.POST['PaymentPhone']

        Customers.objects.filter(id=customerID).update(FirstName=request.POST['firstName'], LastName=request.POST['lastName'], Phone=request.POST['Phone'], Email=request.POST['Email'], Password=request.POST['Password'],
                              Payment_Type=request.POST['PaymentMethod'], Address=request.POST['Address'], Card_no=AccountNo, Card_cvs=CVC, Card_exp=ExpireDate, PaymentPhone=Payment_Phone)
        messages.success(request,"Updated")
        return redirect('CustomerAccount')

@Admin_login_required
def AdminBlogs(request):
    info = Blog.objects.all()
    return render(request,"Dashboard/AdminBlogs.html",{'info':info})

@Admin_login_required
def AddBlog(request):
    if request.method=="POST":
        result = Blog(Title=request.POST['Title'],Description=request.POST['description'],
            Image=request.FILES['Image'])
        result.save()
        messages.success(request,"Inserted")
        return redirect('AdminBlogs')

@Admin_login_required
def AdminContacts(request):
    info = Contacts.objects.all()
    return render(request,"Dashboard/AdminContacts.html",{'info':info})


def ViewBlog(request):
    info = Blog.objects.all()
    return render(request,"home/blogs.html",{'info':info})

def Customer_Contact(request):
    return render(request,"home/Customer_Contact.html")

def SaveContact(request):
    if request.method == "POST":
        result = Contacts(Name=request.POST['name'],Email=request.POST['email'], Subject=request.POST['subject'], Message=request.POST['message'])
        result.save()
        messages.success(request,"Saved Thank you")
        return redirect('home')

@Admin_login_required
def DeleteFunction(request, type, id):
    if type == 'Contact':
        Contacts.objects.filter(id=id).delete()
        messages.success(request,"Deleted")
        return redirect('AdminContacts')
    if type == 'Blogs':
        Blog.objects.filter(id=id).delete()
        messages.success(request,"Deleted")
        return redirect('AdminBlogs')
    if type == 'CustomerAccount':
        Customers.objects.filter(id=id).delete()
        messages.success(request,"Deleted")
        return redirect('CustomersAccounts')
    if type == "adminAccount":
        Admin_Account.objects.filter(id=id).delete()
        messages.success(request,"Deleted")
        return redirect('AdminAccounts')
    if type == "product":
        Products.objects.filter(id=id).delete()
        messages.success(request,"Deleted")
        return redirect('AllProducts')
    if type == "Category":
        Categories.objects.filter(id=id).delete()
        messages.success(request,"Deleted")
        return redirect('AllProducts')
    if type == "gallery":
        Galleries.objects.filter(id=id).delete()
        messages.success(request,"Deleted")
        return redirect('AllProducts')
    if type == "shipping":
        Shipping.objects.filter(id=id).delete()
        messages.success(request,"Deleted")
        return redirect('AdminShipping')
    else:
        messages.success(request,"Error")
        return redirect('Dashboard')
    


def UpdateCategory(request, id):
    Categories.objects.filter(id=id).update(name=request.POST['CategoryName'])
    messages.success(request,"Updated")
    return redirect(request.META.get('HTTP_REFERER'))

def UpdateProduct(request, id):
    info = Products.objects.get(id=id)
    if request.method == "POST":
        if len(request.FILES) != 0:
            info.Image = request.FILES['Images']
        info.Product_Name=request.POST['ProductName']
        info.Description=request.POST['Description']
        info.Price=request.POST['Price']
        info.Quantity=request.POST['Quantity']
        info.Stock=request.POST['InStock']
        info.categories_id_id=request.POST['CategoryID']
        info.save()
        messages.success(request, "Product Updated")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))


@Admin_login_required
def UpdateBlog(request, id):
    info = Blog.objects.get(id=id)
    if request.method=="POST":
        if len(request.FILES) != 0:
            info.Image = request.FILES['Image']
        info.Title=request.POST['Title']
        info.Description=request.POST['description']
        info.save()
        messages.success(request,"Inserted")
        return redirect('AdminBlogs')


def AddAdminAccount(request):
    if request.method == "POST":
        result = Admin_Account(Permission=request.POST['role'], Username=request.POST['Username'],Email=request.POST['Email'],Password=request.POST['Password'],Status='Offline')
        result.save()
        messages.success(request,"Added")
        return redirect('AdminAccounts')

@Admin_login_required
def EditAdminAccount(request, id):
    if request.method == "POST":
        result = Admin_Account.objects.filter(id=id).update(Username=request.POST['Username'],Email=request.POST['Email'],Password=request.POST['Password'],Permission='7',Status='Offline')
        messages.success(request,"Added")
        return redirect('AdminAccounts')

@Admin_login_required
def AdminShipping(request):
    info = Shipping.objects.all()
    return render(request,"Dashboard/AdminShipping.html",{'info':info})

@Admin_login_required
def AddNewShipping(request):
    if request.method == "POST":
        result = Shipping(Shipping_Type=request.POST['Shipping_Type'],
            Shipping_Zone=request.POST['Shipping_Zone'],Price=request.POST['Price'])
        result.save()
        messages.success(request,"Added")
        return redirect('AdminShipping')

@Admin_login_required
def EditShipping(request, id):
    if request.method == "POST":
        result = Shipping.objects.filter(id=id).update(Shipping_Type=request.POST['Shipping_Type'],Shipping_Zone=request.POST['Shipping_Zone'],Price=request.POST['Price'])
        messages.success(request,"Added")
        return redirect('AdminShipping')

def changeOrderStatus(request, status, id):
    Orders.objects.filter(id=id).update(Status=status)
    messages.success(request,"Changed")
    return redirect(request.META.get('HTTP_REFERER'))

def removeCart(request, id):
    Orders.objects.filter(id=id).delete()
    messages.success(request,"Product Removed Successfully")
    return redirect(request.META.get('HTTP_REFERER'))

# Seller

def sellerAccount(request):
    return render(request, 'home/seller_account.html')

def registerSeller(request):
    if request.method == "POST":
        Seller(
            firstname= request.POST['firstname'],
            lastname= request.POST['lastname'],
            email = request.POST['email'],
            password = request.POST['password']
        ).save()
        messages.success(request,"Seller Account Registered")
        return redirect('seller.account')

    else:
        messages.success(request,"Seller s Registered")
        return redirect('seller.account')


def loginSeller(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        
        if Seller.objects.filter(email=username).exists():
            user = Seller.objects.get(email=username)
            if user.password == password:
                request.session['seller']  = 1
                request.session['seller_id']  = user.id
                request.session['firstname'] = user.firstname
                request.session['lastname'] = user.lastname
                request.session['email'] = user.email
                messages.success(request, 'Welcome')
                return redirect('seller.home')
            else:
                messages.error(request, "Incorrect Username or Password")
                return redirect('seller.account')
        else:
            messages.error(request, "Incorrect Username or Password")
            return redirect('seller.account')
    else:
        messages.error(request, "Incorrect Username or Password")
        return redirect('seller.account')


def sellerHome(request):
    productt = Products.objects.all().count()
    Customer = Customers.objects.all().count()
    Order = Orders.objects.all().count()
    Contact = Contacts.objects.all().count()
    blog = Blog.objects.all().count()
    AdminAccount = Admin_Account.objects.all().count()
    Gallery = Galleries.objects.all().count()

    return render(request, "Dashboard/seller_home.html",{'Gallery':Gallery, 'AdminAccount':AdminAccount, 'blog':blog, 'productt':productt,'Customer':Customer,'Order':Order,'Contact':Contact})


def showProduct(request):
    sid = request.session['seller_id']
    Categories_ = Categories.objects.filter(seller_id=sid).reverse()
    Products_ = Products.objects.filter(seller_id=sid).reverse()
    Gallery = Galleries.objects.all()
    return render(request, "Dashboard/seller_products.html", {'Categories_': Categories_, 'Products_': Products_, 'Gallery': Gallery})

def showSelOrders(request):
    sid = request.session['seller_id']
    productsList = Products.objects.filter(seller_id=sid)
    shipmentList = Shipping.objects.all()
    RefundsInfo = Refunds.objects.all()
    Customer = Customers.objects.all()

    result = Orders.objects.all().select_related('Products_id')
    return render(request, "Dashboard/seller_order.html", {'Customer':Customer, 'OrderInfo': result, 'shipmentList': shipmentList, 'productsList': productsList, 'RefundsInfo': RefundsInfo})


def sellerLogout(request):
    del request.session['seller_id']
    del request.session['firstname']
    del request.session['lastname']
    del request.session['email']
    del request.session['seller']
    return redirect('seller.account')