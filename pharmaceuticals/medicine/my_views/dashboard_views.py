from matplotlib.style import available
from medicine.models import *
from django.shortcuts import render, redirect
from django.http import JsonResponse


def home(request):
    available_stock = count_total_stock()
    return render(request, 'medicine/dashboard/dashboard.html', {'available_stock':int(available_stock)})

def count_total_stock():
    available = 0
    total = 0
    medicines = Medicine.objects.filter(archive=False).all()
    for medicine in medicines:
        available = available + medicine.quantity
        total = total + medicine.remaining
    return available*100/total


# bar chat ajax
def stock_statistics(request):
    medicine_statistics = Medicine.objects.filter(archive=False).values()
    data = []
    labels = []
    for ms in medicine_statistics:
        data.append(ms['quantity'])
        labels.append(ms['brand_name'])

    return JsonResponse({'labels':labels, 'data':data})
    

def remaining_stock(request):
    medicines = Medicine.objects.filter(archive=False).all()
    return render(request, 'medicine/dashboard/stock_statistics.html', {'medicines':medicines})
