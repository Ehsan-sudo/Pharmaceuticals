from medicine.models import *
from django.shortcuts import render, redirect
from django.contrib import messages

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