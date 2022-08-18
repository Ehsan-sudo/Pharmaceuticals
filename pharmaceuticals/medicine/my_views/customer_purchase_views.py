from medicine.models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
import json
import re


# CUSTOMER PURCHASE START ========================================>>
def list_customer_purchase(request):
    companies = CustomerPurchase.objects.all()
    paginator = Paginator(companies, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'medicine/customer_purchase/list_customer_purchase.html', {'page_obj':page_obj})

def customer_purchase(request):
    medicines = Medicine.objects.all()
    customers = Customer.objects.all()
    return render(request, 'medicine/customer_purchase/add_customer_purchase.html', {'medicines':medicines, 'customers':customers})

            # only called by ajax while adding new bill
def add_customer_purchase(request):
    received_data = json.loads(request.body)
    customer_purchase = CustomerPurchase.objects.create(customer_id=int(received_data['customer']))
    for selection in received_data['selections']:
        medicine = Medicine.objects.get(pk=int(selection['id']))
        medicine.quantity = medicine.quantity - int(selection['quantity'])
        medicine.save()
        cpm = CustomerPurchaseMedicine.objects.create(medicine=medicine, purchase=customer_purchase, quantity=int(selection['quantity']), unit_price=float(selection['price']))
        print('SUCCESS!')
    customer = Customer.objects.get(pk=int(received_data['customer']))
    customer.debt = customer.debt + int(received_data['grandTotal'])
    customer.save()
    return JsonResponse({'customer_purchase_id':customer_purchase.id})

def edit_customer_purchase(request, id):
    requested_html = re.search(r'^text/html', request.META.get('HTTP_ACCEPT'))
    customer_purchase = CustomerPurchase.objects.get(pk=id)
    if not requested_html:
        received_data = json.loads(request.body)
        # undoing changes
        total = 0
        for med in customer_purchase.medicines.all():
            medicine = Medicine.objects.get(pk=med.medicine.id)
            medicine.quantity = medicine.quantity + med.quantity
            medicine.save()
            total = total + (med.unit_price*med.quantity)
        customer = Customer.objects.get(pk=customer_purchase.customer.id)
        customer.debt = customer.debt - total
        customer.save()

        # deleting previous records
        customer_purchase.medicines.all().delete()
        
        # adding new records
        new_customer = Customer.objects.get(pk=received_data['customer'])
        customer_purchase.customer = new_customer
        for selection in received_data['selections']:
            medicine = Medicine.objects.get(pk=int(selection['id']))
            medicine.quantity = medicine.quantity - int(selection['quantity'])
            medicine.save()
            cpm = CustomerPurchaseMedicine.objects.create(medicine=medicine, purchase=customer_purchase, quantity=int(selection['quantity']), unit_price=float(selection['price']))
        new_customer.debt = customer.debt + int(received_data['grandTotal'])
        new_customer.save()
        customer_purchase.save()
        return JsonResponse({'url':f'127.0.0.1:8000/get-customer-purchase/{customer_purchase.id}'})
    else:
        customers = Customer.objects.all()
        medicines = Medicine.objects.all()
        selected_medicines = customer_purchase.medicines.all()
        selected_customer = customer_purchase.customer
        if customer_purchase:
            return render(request, 'medicine/customer_purchase/edit_customer_purchase.html', {'customer_purchase':customer_purchase, 'customers':customers, 'medicines':medicines, 'selected_medicines':selected_medicines, 'selected_customer':selected_customer})
        else:
            return redirect('page_404')

def get_customer_purchase(request, id):
    if CustomerPurchase.objects.filter(id=id).exists():
        customer_purchase = CustomerPurchase.objects.get(pk=id)
        medicines = customer_purchase.medicines.all()
        total = 0
        for medicine in medicines:
            total += medicine.unit_price * medicine.quantity
        return render(request, 'medicine/customer_purchase/get_customer_purchase.html', {'customer_purchase':customer_purchase, 'medicines':medicines, 'total':total})
    else:
        return redirect('page_404')

def delete_customer_purchase(request,id):
    customer_purchase = CustomerPurchase.objects.get(pk=id)
    total = 0
    if customer_purchase:
        for med in customer_purchase.medicines.all():
            medicine = Medicine.objects.get(pk=med.medicine.id)
            medicine.quantity = medicine.quantity + med.quantity
            medicine.save()
            total = total + (med.unit_price*med.quantity)
        customer = Customer.objects.get(pk=customer_purchase.customer.id)
        customer.debt = customer.debt - total
        customer.save()
        customer_purchase.delete()
        return redirect('list_customer_purchase')
    else:
        return redirect('page_404')

def search_customer_purchase(request):
    # validations
    search_value_post = request.POST.get('search_value')
    search_value_get = request.GET.get('search_value')
    search_value = None
    if search_value_post:
        search_value = search_value_post
    else:
        search_value = search_value_get
    if search_value:
        customers = Customer.objects.filter(name__icontains=search_value).all()
        customer_purchase = []
        for customer in customers:
            for p in customer.purchases.all():
                customer_purchase.append(p)
        paginator = Paginator(customer_purchase, 10) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if customers:
            messages.success(request, f'د {search_value} په اړه معلومات پیدا سول!')
        else:
            messages.warning(request, 'غوښتل سوي معلومات شتون نه لري!')
        return render(request, 'medicine/customer_purchase/list_customer_purchase.html', {'page_obj':page_obj, 'search_value':search_value})
    else:
        return redirect('page_404')

# CUSTOMER PURCHASE END ==========================================>>