from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('list-company/', views.list_company, name='list_company'),
    path('list-company/<int:id>/', views.get_company, name='get_company'),
    path('add-company/', views.add_company, name='add_company'),
    path('delete-company/<int:id>/', views.delete_company, name='delete_company'),

    path('not-found-404/', views.page_404, name='page_404'),

]