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

    # customer routes
    path('list-customer/', views.list_customer, name='list_customer'),
    path('edit-customer/<int:id>/', views.edit_customer, name='edit_customer'),
    path('get-customer/<int:id>/', views.get_customer, name='get_customer'),
    path('add-customer/', views.add_customer, name='add_customer'),
    path('delete-customer/<int:id>/', views.delete_customer, name='delete_customer'),

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
    
    path('not-found-404/', views.page_404, name='page_404'),

]