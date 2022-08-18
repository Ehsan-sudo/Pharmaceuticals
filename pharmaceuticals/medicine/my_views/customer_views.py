from medicine.models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator


# CUSTOMER VIEWS START ===========================================>>
def list_customer(request):
    customers = Customer.objects.all()
    paginator = Paginator(customers, 5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'medicine/customer/list_customer.html', {'page_obj':page_obj})

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

def search_customer(request):
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
        paginator = Paginator(customers, 5) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if customers:
            messages.success(request, f'د {search_value} لپاره معلومات پیدا سول!')
        else:
            messages.warning(request, 'غوښتل سوي معلومات شتون نه لري!')
        return render(request, 'medicine/customer/list_customer.html', {'page_obj':page_obj, 'search_value':search_value})
    else:
        return redirect('page_404')
# CUSTOMER VIEWS END =============================================>>