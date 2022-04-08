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

    path('not-found-404/', views.page_404, name='page_404'),

]