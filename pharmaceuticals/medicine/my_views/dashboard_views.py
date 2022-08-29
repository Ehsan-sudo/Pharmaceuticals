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

    # remaining debts
    remaining_debt = Customer.objects.aggregate(Sum('debt'))['debt__sum']

    # collected payments
    # this need archived filter
    collected_payment = CustomerPayment.objects.aggregate(Sum('paid_amount'))['paid_amount__sum']

    return render(request, 'medicine/dashboard/dashboard.html', {'available_stock':int(available_stock), 'p_m_sales':total, 'remaining_debt':remaining_debt, 'collected_payment':collected_payment})
    

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

def debt(request):
    customers = Customer.objects.filter(debt__gt=0).all().order_by('-debt')
    data = []
    labels = []
    for customer in customers:
        data.append(customer.debt)
        labels.append(str(customer.name))
    return render(request, 'medicine/dashboard/debt.html', {'customers':customers, 'data':data, 'labels':labels})


def payment_statistics(request):
    if request.method == 'GET':
        from_date = datetime.timedelta(days = 30)
        to_date = datetime.datetime.now()
        date_range = to_date - from_date
        date_range = date_range.strftime('%Y-%m-%d')
        # this should be filtered with archive
        collected_payments = CustomerPayment.objects.raw(f"select c.id, c.name,  sum(cp.paid_amount) as total from medicine_customerpayment as cp join medicine_customer as c on cp.customer_id = c.id where cp.date > '{date_range}' group by c.id")
        messages.success(request, 'تاسي د تېري میاشتي پېمنټ وینئ!')
    else:
        # validations
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        date_range = None
        if not to_date:
            to_date = datetime.datetime.now().date()
            to_date = to_date.strftime('%Y-%m-%d')
            print(f'THISZZZ {to_date}')
        collected_payments = CustomerPayment.objects.raw(f"select c.id, c.name,  sum(cp.paid_amount) as total from medicine_customerpayment as cp join medicine_customer as c on cp.customer_id = c.id where (cp.date BETWEEN '{from_date}' AND'{to_date}') group by c.id")
        messages.success(request, f'تاسي د {from_date} څخه تر {to_date} پوري پېمنټ وینئ!')
    total = 0
    for cp in collected_payments:
        total = total + cp.total
    return render(request, 'medicine/dashboard/payment_statistics.html', {'collected_payments':collected_payments, 'total':total, 'date_range':date_range, 'from_date':from_date, 'to_date':to_date})
