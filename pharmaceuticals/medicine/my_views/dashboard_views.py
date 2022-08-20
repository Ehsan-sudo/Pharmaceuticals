from matplotlib.style import available
from medicine.models import *
from django.shortcuts import render, redirect


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

    