from medicine.models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.db.models import Q


# MEDICINE START =================================================>>
def list_medicine(request, type):
    medicines = None
    if type == 0:
        medicines = Medicine.objects.all()
    else:
        medicines = Medicine.objects.filter(archive=False).all()
    paginator = Paginator(medicines, 5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'medicine/medicine/list_medicine.html', {'page_obj':page_obj})


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
        remaining = request.POST.get('quantity')
        company_purchase = CompanyPurchase.objects.get(pk=request.POST.get('company_purchase'))
        # validation missing: check if the uploaded file is an image
        if request.FILES.get('medicine_img'):
            upload = request.FILES['medicine_img']
            fss = FileSystemStorage()
            file = fss.save(upload.name, upload)
            image = fss.url(file)
        else:
            image = '/media/default.jpg'

        medicine = Medicine.objects.create(
            brand_name=brand_name,
            medical_name=medical_name,
            formula=formula,
            type=type,
            expire_date=expire_date,
            in_price=in_price,
            out_price=out_price,
            quantity=quantity,
            remaining=remaining,
            company_purchase=company_purchase,
            image=image
        )
        messages.success(request, 'معلومات په بریالیتوب سره اضافه سول!')
        return redirect('list_medicine', type=1)
    else:
        company_purchases = CompanyPurchase.objects.all()
        medicine_types = MedicineType.objects.all()
        return render(request, 'medicine/medicine/add_medicine.html', {'medicine_types':medicine_types, 'company_purchases':company_purchases})

def edit_medicine(request, id):
    medicine = Medicine.objects.get(pk=id)
    if medicine:
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
            company_purchase = CompanyPurchase.objects.get(pk=request.POST.get('company_purchase'))
            medicine.company_purchase = company_purchase
            medicine.save()
            messages.success(request, f'معلومات په بریالیتوب سره نوي سول!')
            return redirect('get_medicine', id=id)
        else:
            company_purchases = CompanyPurchase.objects.all()
            medicine_types = MedicineType.objects.all()
            return render(request, 'medicine/medicine/edit_medicine.html', {'medicine':medicine, 'company_purchases':company_purchases, 'medicine_types':medicine_types})
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
        return redirect('list_medicine', type=1)
    else:
        return redirect('page_404')

def search_medicine(request):
    # validations
    search_value_post = request.POST.get('search_value')
    search_value_get = request.GET.get('search_value')
    search_value = None
    if search_value_post:
        search_value = search_value_post
    else:
        search_value = search_value_get
    if search_value:
        medicines = Medicine.objects.filter(Q(brand_name__icontains=search_value) | Q(medical_name__icontains=search_value)).all()
        
        paginator = Paginator(medicines, 5) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if medicines:
            messages.success(request, f'د {search_value} لپاره معلومات پیدا سول!')
        else:
            messages.warning(request, 'غوښتل سوي معلومات شتون نه لري!')
        return render(request, 'medicine/medicine/list_medicine.html', {'page_obj':page_obj, 'search_value':search_value})
    else:
        return redirect('page_404')

def archive_medicine(request, id):
    # validation & only post reqeust
    medicine = Medicine.objects.get(pk=id)
    if medicine:
        medicine.archive = True
        medicine.save()
        return redirect('get_medicine', id=id)
    return redirect('page_404')

def unarchive_medicine(request, id):
    # validation & only post reqeust
    medicine = Medicine.objects.get(pk=id)
    if medicine:
        medicine.archive = False
        medicine.save()
        return redirect('get_medicine', id=id)
    return redirect('page_404')
    
# MEDICINE END ===================================================>>