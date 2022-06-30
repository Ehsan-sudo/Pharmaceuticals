from medicine.models import *
from django.shortcuts import render, redirect
from django.contrib import messages

# COMPANY PURCHASE VIEWS START
def list_company_purchase(request):
    company_purchases = CompanyPurchase.objects.all()
    return render(request, 'medicine/company_purchase/list_company_purchase.html', {'company_purchases':company_purchases})

def add_company_purchase(request):
    if request.POST:
        # data validation missing   
        company = Company.objects.get(pk=request.POST.get('company'))
        date = request.POST.get('date')
        CompanyPurchase.objects.create(company=company, date=date)  
        messages.success(request, 'معلومات په بریالیتوب سره اضافه سول!')
        return redirect('list_company_purchase')
    companies = Company.objects.all()
    return render(request, 'medicine/company_purchase/add_company_purchase.html', {'companies':companies})

def edit_company_purchase(request, id):
    if request.POST:
        # data validation missing
        company.name = request.POST.get('name')
        company.email = request.POST.get('email')
        company.phone = request.POST.get('phone')
        company.location = request.POST.get('location')
        company.save()
        messages.success(request, f'معلومات په بریالیتوب سره نوي سول!')
        return redirect('get_company', id=id) 
  
    company_purchase = CompanyPurchase.objects.get(pk=id)
    medicines = company_purchase.medicines.all()
    companies = Company.objects.all()
    date = str(company_purchase.date)
    return render(request, 'medicine/company_purchase/edit_company_purchase.html', {'company_purchase':company_purchase, 'companies':companies, 'date':date, 'medicines':medicines})

def get_company_purchase(request, id):
    company_purchase = CompanyPurchase.objects.get(pk=id)
    if company_purchase:
        return render(request, 'medicine/company_purchase/get_company_purchase.html', {'company_purchase':company_purchase})
    else:
        return redirect('page_404')

def delete_company_purchase(request, id):
    if Company.objects.filter(id=id).exists():
        Company.objects.get(pk=id).delete()
        messages.warning(request, 'معلومات په بریالیتوب سره ډیلیټ سول!')
        return redirect('list_company')
    else:
        return redirect('page_404')
# COMPANY PURCHASE VIEWS END