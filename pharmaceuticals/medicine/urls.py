from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),

    # company routes
    path('list-company/', views.list_company, name='list_company'),
    path('edit-company/<int:id>/', views.edit_company, name='edit_company'),
    path('get-company/<int:id>/', views.get_company, name='get_company'),
    path('add-company/', views.add_company, name='add_company'),
    path('delete-company/<int:id>/', views.delete_company, name='delete_company'),

    # company purchase routes
    path('list-company-purchase/', views.list_company_purchase, name='list_company_purchase'),
    path('edit-company-purchase/<int:id>/', views.edit_company_purchase, name='edit_company_purchase'),
    path('get-company-purchase/<int:id>/', views.get_company_purchase, name='get_company_purchase'),
    path('add-company-purchase/', views.add_company_purchase, name='add_company_purchase'),
    path('delete-company-purchase/<int:id>/', views.delete_company_purchase, name='delete_company_purchase'),
    
    # customer routes
    path('list-customer/', views.list_customer, name='list_customer'),
    path('edit-customer/<int:id>/', views.edit_customer, name='edit_customer'),
    path('get-customer/<int:id>/', views.get_customer, name='get_customer'),
    path('add-customer/', views.add_customer, name='add_customer'),
    path('delete-customer/<int:id>/', views.delete_customer, name='delete_customer'),

    # customer purchase routes
    path('list-customer-purchase/', views.list_customer_purchase, name='list_customer_purchase'),
    path('edit-customer-purchase/<int:id>/', views.edit_customer_purchase, name='edit_customer_purchase'),
    path('get-customer-purchase/<int:id>/', views.get_customer_purchase, name='get_customer_purchase'),
    path('customer-purchase/', views.customer_purchase, name='customer_purchase'),
    path('add-customer-purchase/', views.add_customer_purchase, name='add_customer_purchase'),
    path('delete-customer-purchase/<int:id>/', views.delete_customer_purchase, name='delete_customer_purchase'),

    # medicine type routes
    path('list-medicine-type/', views.list_medicine_type, name='list_medicine_type'),
    path('edit-medicine-type/<int:id>/', views.edit_medicine_type, name='edit_medicine_type'),
    path('get-medicine-type/<int:id>/', views.get_medicine_type, name='get_medicine_type'),
    path('add-medicine-type/', views.add_medicine_type, name='add_medicine_type'),
    path('delete-medicine-type/<int:id>/', views.delete_medicine_type, name='delete_medicine_type'),

    # medicine routes
    path('list-medicine/', views.list_medicine, name='list_medicine'),
    path('edit-medicine/<int:id>/', views.edit_medicine, name='edit_medicine'),
    path('get-medicine/<int:id>/', views.get_medicine, name='get_medicine'),
    path('add-medicine/', views.add_medicine, name='add_medicine'),
    path('delete-medicine/<int:id>/', views.delete_medicine, name='delete_medicine'),
     

    # utility routes
    path('not-found-404/', views.page_404, name='page_404'),

]