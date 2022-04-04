from django.shortcuts import render

# Create your views here.


# to find the total amount of a customer's purchase
# 
# from django.db.models import F
# customer.purchases.get(pk=1).medicines.aggregate(sum=Sum(F('unit_price')*F('quantity')))
