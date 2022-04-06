from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('list-company/', views.list_company, name='list_company'),
    path('add-company/', views.add_company, name='add_company'),
]