from medicine.models import *
from django.shortcuts import render, redirect
from django.contrib import messages


# CUSTOMER PAYMENT START ===============================>>
def list_customer_payment(request):
    customer_payments = CustomerPayment.objects.all()
    return render(request, 'medicine/customer_payment/list_customer_payment.html', {'customer_payments':customer_payments})

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
# CUSTOMER PAYMENT END =================================>>