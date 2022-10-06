from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('Account',views.Account,name="Account"),
    path('Dashboard',views.Dashboard, name="Dashboard"),
    path('Dashboard_Login',views.Dashboard_Login, name="Dashboard_Login"),
    path('Admin_Login',views.Admin_Login, name="Admin_Login"),
    path('Dashboard_Logout',views.Dashboard_Logout, name="Dashboard_Logout"),
    path('AdminAccounts',views.AdminAccounts, name="AdminAccounts"),
    path('RegisterAccount',views.RegisterAccount, name="RegisterAccount"),
    path('CustomersAccounts/',views.CustomersAccounts,name="CustomersAccounts"),
    path('CustomerLogin',views.CustomerLogin,name="CustomerLogin"),
    path('Customerlogout',views.Customerlogout, name="Customerlogout"),
    path('AllProducts',views.AllProducts,name="AllProducts"),
    path('AddCategory',views.AddCategory,name="AddCategory"),
    path('AddProduct',views.AddProduct,name="AddProduct"),
    path('Products_details/<str:id>/',views.Products_details, name="Products_details"),
    path('UploadGallery',views.UploadGallery, name="UploadGallery"),
    path('AddOrders/<str:productID>/',views.AddOrders, name="AddOrders"),
    path('AddOrder',views.AddOrder, name="AddOrder"),
    path('CustomerAccount',views.CustomerAccount, name="CustomerAccount"),
    path('CancelOrder/<str:id>/',views.CancelOrder, name="CancelOrder"),
    path('CancelRequest/<str:id>/',views.CancelRequest, name="CancelRequest"),
    path('AdminOrders',views.AdminOrders, name="AdminOrders"),
    path('Change_Refund_Status/<str:status>/<str:id>/',views.Change_Refund_Status, name="Change_Refund_Status"),
    path('UpdateCustomer',views.UpdateCustomer, name="UpdateCustomer"),
    path('AdminBlogs',views.AdminBlogs, name="AdminBlogs"),
    path('AddBlog',views.AddBlog, name="AddBlog"),
    path('AdminContacts',views.AdminContacts, name="AdminContacts"),
    path('ViewBlog',views.ViewBlog, name="ViewBlog"),
    path('Customer_Contact',views.Customer_Contact, name="Customer_Contact"),
    path('SaveContact',views.SaveContact, name="SaveContact"),
    path('DeleteFunction/<str:type>/<str:id>/',views.DeleteFunction, name="DeleteFunction"),
    path('UpdateCategory/<str:id>/',views.UpdateCategory, name="UpdateCategory"),
    path('UpdateProduct/<str:id>/',views.UpdateProduct, name="UpdateProduct"),
    path('UpdateBlog/<str:id>/',views.UpdateBlog, name="UpdateBlog"),
    path('AddAdminAccount',views.AddAdminAccount, name="AddAdminAccount"),
    path('EditAdminAccount/<str:id>/',views.EditAdminAccount, name="EditAdminAccount"),
    path('AdminShipping',views.AdminShipping, name="AdminShipping"),
    path('AddNewShipping',views.AddNewShipping, name="AddNewShipping"),
    path('EditShipping/<str:id>/',views.EditShipping, name="EditShipping"),
    path('changeOrderStatus/<str:status>/<str:id>/',views.changeOrderStatus, name="changeOrderStatus"),
    path('Shop',views.Shop, name="Shop"),
    path('SearchCategory/<str:id>/',views.SearchCategory, name="SearchCategory"),
    path('about',views.About, name="About"),
    path('remove-cart/<str:id>', views.removeCart , name="remove"),


    # Seller Account
    path('seller', views.sellerAccount , name="seller.account"),
    path('registerseller', views.registerSeller , name="seller.register"),
    path('loginseller', views.loginSeller , name="seller.login"),
    path('seller-home', views.sellerHome , name="seller.home"),

    path('seller-products', views.showProduct , name="seller.products"),
    path('seller-orders', views.showSelOrders , name="seller.orders"),
    path('seller-logout', views.sellerLogout , name="seller.logout"),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
