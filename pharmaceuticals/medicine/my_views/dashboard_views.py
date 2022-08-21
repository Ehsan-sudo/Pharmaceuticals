from matplotlib.style import available
from medicine.models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum, Q
import datetime

from medicine.my_views.customer_purchase_views import customer_purchase

def home(request): 
    # available stock percentage
    available = 0
    total = 0
    medicines = Medicine.objects.filter(archive=False).all()
    for medicine in medicines:
        available = available + medicine.quantity
        total = total + medicine.remaining
    available_stock = available*100/total

    # previous month sales
    last_30 = datetime.datetime.now() - datetime.timedelta(days = 30)
    customer_purchases = CustomerPurchase.objects.filter(date__gte=last_30).all()
    total = 0
    for cp in customer_purchases:
        for cpm in cp.medicines.all():
            total = total + (cpm.quantity*cpm.unit_price)

    return render(request, 'medicine/dashboard/dashboard.html', {'available_stock':int(available_stock), 'p_m_sales':total})
    

def remaining_stock(request):
    medicines = Medicine.objects.filter(archive=False).all()
    data = []
    labels = []
    for ms in medicines:
        data.append(ms.quantity)
        labels.append(str(ms.brand_name))
    messages.success(request, 'تاسي د شته درملو شمېر ګورئ!')
    return render(request, 'medicine/dashboard/stock_statistics.html', {'medicines':medicines, 'data':data, 'labels':labels})

def sales_statistics(request):
    customer_purchases = None
    if request.method == 'GET':
        date_range = datetime.datetime.now() - datetime.timedelta(days = 30)
        customer_purchases = CustomerPurchase.objects.filter(date__gte=date_range).all()
        messages.success(request, 'تاسي د تېري میاشتي خرڅلاو وینئ!')
    else:
        # validations
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        if not to_date:
            to_date = datetime.datetime.now().date()
        customer_purchases = CustomerPurchase.objects.filter(date__gte=from_date, date__lte=to_date).all()
        messages.success(request, f'تاسي د {from_date} څخه تر {to_date} پوري خرڅلاو وینئ!')
    
    total = 0
    benefit = 0
    for cp in customer_purchases:
        for medicine in cp.medicines.all():
            total = total + (medicine.quantity*medicine.unit_price)
            added_value = medicine.unit_price - medicine.medicine.in_price
            benefit = benefit + (added_value*medicine.quantity)

    return render(request, 'medicine/dashboard/previous_month_sales.html', {'customer_purchases':customer_purchases, 'total':total, 'benefit':benefit})
    