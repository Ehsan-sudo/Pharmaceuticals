from medicine.models import *
from django.shortcuts import render, redirect
from django.contrib import messages

# CUSTOMER VIEWS START ===========================================>>
def list_customer(request):
    customers = Customer.objects.all()
    return render(request, 'medicine/customer/list_customer.html', {'customers':customers})

def add_customer(request):
    if request.POST:
        # data validation missing
        name = request.POST.get('name')
        company = request.POST.get('company')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        Customer.objects.create(name=name, company_name=company, email=email, phone=phone, address=address)
        messages.success(request, 'معلومات په بریالیتوب سره اضافه سول!')
        return redirect('list_customer')
    else:
        return render(request, 'medicine/customer/add_customer.html')

def edit_customer(request, id):
    if Customer.objects.filter(id=id).exists():
        customer = Customer.objects.get(pk=id)

        if request.POST:
            # data validation missing
            customer.name = request.POST.get('name')
            customer.company_name = request.POST.get('company')
            customer.email = request.POST.get('email')
            customer.phone = request.POST.get('phone')
            customer.address = request.POST.get('address')
            customer.debt = request.POST.get('debt')
            customer.save()
            messages.success(request, f'معلومات په بریالیتوب سره نوي سول!')
            return redirect('get_customer', id=id)
        else:
            return render(request, 'medicine/customer/edit_customer.html', {'customer':customer})
    else:
        return redirect('page_404')

def get_customer(request, id):
    if Customer.objects.filter(id=id).exists():
        customer = Customer.objects.get(pk=id)
        return render(request, 'medicine/customer/get_customer.html', {'customer':customer})
    else:
        return redirect('page_404')

def delete_customer(request, id):
    if Customer.objects.filter(id=id).exists():
        Customer.objects.get(pk=id).delete()
        messages.warning(request, 'معلومات په بریالیتوب سره ډیلیټ سول!')
        return redirect('list_customer')
    else:
        return redirect('page_404')
# CUSTOMER VIEWS END =============================================>>