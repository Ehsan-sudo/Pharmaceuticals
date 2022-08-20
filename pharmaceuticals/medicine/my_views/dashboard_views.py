from medicine.models import *
from django.shortcuts import render, redirect


def home(request):

    return render(request, 'medicine/dashboard/dashboard.html')


def count_total_stock():
    count = 0
    pass