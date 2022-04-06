from django.shortcuts import render

# Create your views here.


# to find the total amount of a customer's purchase
# 
# from django.db.models import F
# customer.purchases.get(pk=1).medicines.aggregate(sum=Sum(F('unit_price')*F('quantity')))


def home(request):
    return render(request, 'medicine/home.html')


def list_company(request):
    return render(request, 'medicine/company/list_company.html')

def add_company(request):
    return render(request, 'medicine/company/add_company.html')