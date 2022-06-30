from medicine.models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator

def home(request):
    return render(request, 'medicine/home.html')

# COMPANY VIEWS START ============================================>>
def list_company(request):
    companies = Company.objects.all()
    paginator = Paginator(companies, 5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'medicine/company/list_company.html', {'page_obj':page_obj})

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