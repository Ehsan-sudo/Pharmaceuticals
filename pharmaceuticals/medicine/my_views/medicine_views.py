from medicine.models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

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
            company_purchase=company_purchase,
            image=image
        )
        messages.success(request, 'معلومات په بریالیتوب سره اضافه سول!')
        return redirect('list_medicine')
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
        return redirect('list_medicine')
    else:
        return redirect('page_404')
# MEDICINE END ===================================================>>