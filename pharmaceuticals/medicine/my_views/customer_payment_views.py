from medicine.models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator


# CUSTOMER PAYMENT START ===============================>>
def list_customer_payment(request):
    payments = CustomerPayment.objects.all()
    paginator = Paginator(payments, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'medicine/customer_payment/list_customer_payment.html', {'page_obj':page_obj})

def add_customer_payment(request):
    if request.POST:
        # data validation missing
        customer = Customer.objects.get(pk=request.POST.get('customer'))
        date = request.POST.get('date')
        payment = request.POST.get('payment')
        CustomerPayment.objects.create(customer=customer, date=date, paid_amount=payment)
        customer.debt = customer.debt - float(payment)
        # check if the debt is ZERO, then adding payment is an error
        customer.save()
        messages.success(request, 'معلومات په بریالیتوب سره اضافه سول!')
        return redirect('get_customer', id=customer.id)
    else:
        customers = Customer.objects.all()
        return render(request, 'medicine/customer_payment/add_customer_payment.html', {'customers':customers})

def edit_customer_payment(request, id):
    customer_payment = CustomerPayment.objects.filter(id=id).first()
    if customer_payment:
        if request.POST:
            # data validation missing
            # undoing changes
            customer = Customer.objects.get(pk=customer_payment.customer.id)
            customer.debt = customer.debt + customer_payment.paid_amount
            customer.save()
            # editing the record
            new_customer = Customer.objects.get(pk=request.POST.get('customer'))
            customer_payment.customer = new_customer
            customer_payment.paid_amount = request.POST.get('payment')
            new_customer.debt = new_customer.debt - float(request.POST.get('payment'))
            customer_payment.date = request.POST.get('date')
            new_customer.save()
            customer_payment.save()

            messages.success(request, f'معلومات په بریالیتوب سره نوي سول!')
            return redirect('get_customer_payment', id=customer_payment.id)
        else:
            customers = Customer.objects.all()
            date = str(customer_payment.date)
            return render(request, 'medicine/customer_payment/edit_customer_payment.html', {'customer_payment':customer_payment, 'customers':customers, 'date':date})
    else:
        return redirect('page_404')

def get_customer_payment(request, id):
    customer_payment = CustomerPayment.objects.filter(id=id).first()
    if customer_payment:
        return render(request, 'medicine/customer_payment/get_customer_payment.html', {'customer_payment':customer_payment})
    else:
        return redirect('page_404')

def delete_customer_payment(request, id):
    customer_payment = CustomerPayment.objects.filter(id=id).first()
    if customer_payment:
        customer = customer_payment.customer
        customer.debt = customer.debt + customer_payment.paid_amount
        customer.save()
        customer_payment.delete() 
        messages.warning(request, 'معلومات په بریالیتوب سره ډیلیټ سول!')
        return redirect('list_customer_payment')
    else:
        return redirect('page_404')

def search_customer_payment(request):
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
        customer_payments = []
        for customer in customers:
            for p in customer.payments.all():
                customer_payments.append(p)
        paginator = Paginator(customer_payments, 10) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if customers:
            messages.success(request, f'د {search_value} په اړه معلومات پیدا سول!')
        else:
            messages.warning(request, 'غوښتل سوي معلومات شتون نه لري!')
        return render(request, 'medicine/customer_payment/list_customer_payment.html', {'page_obj':page_obj, 'search_value':search_value})
    else:
        return redirect('page_404')

# CUSTOMER PAYMENT END =================================>>