from django.shortcuts import render, redirect
from django.contrib import messages
from medicine.models import Company, Customer, MedicineType

# Create your views here.


# to find the total amount of a customer's purchase
# 
# from django.db.models import F
# customer.purchases.get(pk=1).medicines.aggregate(sum=Sum(F('unit_price')*F('quantity')))


def home(request):
    return render(request, 'medicine/home.html')

# COMPANY VIEWS START ============================================>>
def list_company(request):
    companies = Company.objects.all()
    return render(request, 'medicine/company/list_company.html', {'companies':companies})

def add_company(request):
    if request.POST:
        # data validation missing
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        Company.objects.create(name=name, email=email, phone=phone, location=location)
        messages.success(request, 'معلومات په بریالیتوب سره اضافه سول!')
        return redirect('list_company')
    return render(request, 'medicine/company/add_company.html')

def edit_company(request, id):
    if Company.objects.filter(id=id).exists():
        company = Company.objects.get(pk=id)

        if request.POST:
            # data validation missing
            company.name = request.POST.get('name')
            company.email = request.POST.get('email')
            company.phone = request.POST.get('phone')
            company.location = request.POST.get('location')
            company.save()
            messages.success(request, f'معلومات په بریالیتوب سره نوي سول!')
            return redirect('get_company', id=id)
        else:
            return render(request, 'medicine/company/edit_company.html', {'company':company})
    else:
        return redirect('page_404')

def get_company(request, id):
    if Company.objects.filter(id=id).exists():
        company = Company.objects.get(pk=id)
        return render(request, 'medicine/company/get_company.html', {'company':company})
    else:
        return redirect('page_404')

def delete_company(request, id):
    if Company.objects.filter(id=id).exists():
        Company.objects.get(pk=id).delete()
        messages.warning(request, 'معلومات په بریالیتوب سره ډیلیټ سول!')
        return redirect('list_company')
    else:
        return redirect('page_404')
# COMAPNY VIEWS  END =============================================>>


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


# MEDICINE TYPE START ============================================>>
def list_medicine_type(request):
    medicine_types = MedicineType.objects.all()
    return render(request, 'medicine/medicine_type/list_medicine_type.html', {'medicine_types':medicine_types})

def add_medicine_type(request):
    if request.POST:
        # data validation missing
        name = request.POST.get('name')
        MedicineType.objects.create(type=name)
        messages.success(request, 'معلومات په بریالیتوب سره اضافه سول!')
        return redirect('list_medicine_type')
    else:
        return render(request, 'medicine/medicine_type/add_medicine_type.html')

def edit_medicine_type(request, id):
    if MedicineType.objects.filter(id=id).exists():
        medicine_type = MedicineType.objects.get(pk=id)

        if request.POST:
            # data validation missing
            medicine_type.type = request.POST.get('name')
            medicine_type.save()
            messages.success(request, f'معلومات په بریالیتوب سره نوي سول!')
            return redirect('get_medicine_type', id=id)
        else:
            return render(request, 'medicine/medicine_type/edit_medicine_type.html', {'medicine_type':medicine_type})
    else:
        return redirect('page_404')

def get_medicine_type(request, id):
    if MedicineType.objects.filter(id=id).exists():
        medicine_type = MedicineType.objects.get(pk=id)
        return render(request, 'medicine/medicine_type/get_medicine_type.html', {'medicine_type':medicine_type})
    else:
        return redirect('page_404')

def delete_medicine_type(request, id):
    if MedicineType.objects.filter(id=id).exists():
        MedicineType.objects.get(pk=id).delete()
        messages.warning(request, 'معلومات په بریالیتوب سره ډیلیټ سول!')
        return redirect('list_medicine_type')
    else:
        return redirect('page_404')

# MEDICINE TYPE END ==============================================>>
def page_404(request):
    return render(request, 'medicine/utility/pages-404.html')