import re
from django.shortcuts import render, redirect
from django.contrib import messages
from medicine.models import Company, Customer, CustomerPurchase, Medicine, MedicineType, CustomerPurchaseMedicine
from django.core.files.storage import FileSystemStorage
from PIL import Image
from django.http import JsonResponse
import json

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

# CUSTOMER PURCHASE START ========================================>>
def list_customer_purchase(request):
    customer_purchases = CustomerPurchase.objects.all()
    return render(request, 'medicine/customer_purchase/list_customer_purchase.html', {'customer_purchases':customer_purchases})

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
        cpm = CustomerPurchaseMedicine.objects.create(medicine=medicine, purchase=customer_purchase, quantity=int(selection['quantity']), unit_price=int(selection['price']))
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
        print(received_data)
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
# CUSTOMER PURCHASE END ==========================================>>

# CUSTOMER PURCHASE MEDICINE START ===============================>>
''' if CustomerPurchaseMedicine.objects.filter(id=id).exists():
        CustomerPurchaseMedicine.objects.get(pk=id).delete()
        messages.warning(request, 'معلومات په بریالیتوب سره ډیلیټ سول!')
        return redirect('list_customer_purchase')
    else:
        return redirect('page_404')'''
# CUSTOMER PURCHASE MEDICINE END =================================>>


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

# MEDICINE START =================================================>>
def list_medicine(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicine/medicine/list_medicine.html', {'medicines':medicines})

def add_medicine(request):
    if request.POST:
        # data validation missing
        med_type_id = request.POST.get('medicine_type')
        brand_name = request.POST.get('brand_name')
        medical_name = request.POST.get('medical_name')
        formula = request.POST.get('formula')
        type = MedicineType.objects.get(pk=med_type_id)
        expire_date = request.POST.get('expire_date')
        in_price = request.POST.get('in_price')
        out_price = request.POST.get('out_price')
        quantity = request.POST.get('quantity')
        # validation missing: check if the uploaded file is an image
        upload = request.FILES['medicine_img']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        image = fss.url(file)

        Medicine.objects.create(
            brand_name=brand_name,
            medical_name=medical_name,
            formula=formula,
            type=type,
            expire_date=expire_date,
            in_price=in_price,
            out_price=out_price,
            quantity=quantity,
            image=image
        )
        messages.success(request, 'معلومات په بریالیتوب سره اضافه سول!')
        return redirect('list_medicine')
    else:
        return render(request, 'medicine/medicine/add_medicine.html', {'medicine_types':MedicineType.objects.all()})

def edit_medicine(request, id):
    if Medicine.objects.filter(id=id).exists():
        medicine = Medicine.objects.get(pk=id)

        if request.POST:
            # data validation missing
            medicine.brand_name = request.POST.get('brand_name')
            medicine.medical_name = request.POST.get('medical_name')
            medicine.formula = request.POST.get('formula')
            medicine.type = MedicineType.objects.get(pk=request.POST.get('medicine_type'))
            if request.POST.get('expire_date') == '':
                medicine.expire_date = '2022-02-02'
            else:
                medicine.expire_date = request.POST.get('expire_date')
            medicine.in_price = request.POST.get('in_price')
            medicine.out_price = request.POST.get('out_price')
            medicine.quantity = request.POST.get('quantity')
            
            medicine.save()
            messages.success(request, f'معلومات په بریالیتوب سره نوي سول!')
            return redirect('get_medicine', id=id)
        else:
            return render(request, 'medicine/medicine/edit_medicine.html', {'medicine':medicine, 'medicine_types':MedicineType.objects.all()})
    else:
        return redirect('page_404')

def get_medicine(request, id):
    if Medicine.objects.filter(id=id).exists():
        medicine = Medicine.objects.get(pk=id)
        return render(request, 'medicine/medicine/get_medicine.html', {'medicine':medicine})
    else:
        return redirect('page_404')

def delete_medicine(request, id):
    if Medicine.objects.filter(id=id).exists():
        Medicine.objects.get(pk=id).delete()
        messages.warning(request, 'معلومات په بریالیتوب سره ډیلیټ سول!')
        return redirect('list_medicine')
    else:
        return redirect('page_404')
# MEDICINE END ===================================================>>

def page_404(request):
    return render(request, 'medicine/utility/pages-404.html')