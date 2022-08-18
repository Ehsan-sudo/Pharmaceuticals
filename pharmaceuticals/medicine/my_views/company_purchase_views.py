from medicine.models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator

# COMPANY PURCHASE VIEWS START
def list_company_purchase(request):
    company_purchases = CompanyPurchase.objects.all()
    paginator = Paginator(company_purchases, 5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'medicine/company_purchase/list_company_purchase.html', {'page_obj':page_obj})

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
    company_purchase = CompanyPurchase.objects.get(pk=id)
    if request.POST:
        # data validation missing
        company_purchase.company = Company.objects.get(pk=request.POST.get('company'))
        company_purchase.date = request.POST.get('date')
        company_purchase.save()
        messages.success(request, f'معلومات په بریالیتوب سره نوي سول!')
        return redirect('get_company_purchase', id=id) 
  
    companies = Company.objects.all()
    date = str(company_purchase.date)
    return render(request, 'medicine/company_purchase/edit_company_purchase.html', {'company_purchase':company_purchase, 'companies':companies, 'date':date})

def get_company_purchase(request, id):
    company_purchase = CompanyPurchase.objects.get(pk=id)
    if company_purchase:
        return render(request, 'medicine/company_purchase/get_company_purchase.html', {'company_purchase':company_purchase})
    else:
        return redirect('page_404')

def delete_company_purchase(request, id):
    company_purchase = CompanyPurchase.objects.get(pk=id)
    if company_purchase:
        company_purchase.delete()
        messages.warning(request, 'معلومات په بریالیتوب سره ډیلیټ سول!')
        return redirect('list_company_purchase')
    else:
        return redirect('page_404')

def search_company_purchase(request):
    # validations
    search_value_post = request.POST.get('search_value')
    search_value_get = request.GET.get('search_value')
    search_value = None
    if search_value_post:
        search_value = search_value_post
    else:
        search_value = search_value_get
    if search_value:
        companies = Company.objects.filter(name__icontains=search_value).all()
        company_purchase = []
        for company in companies:
            for p in company.purchases.all():
                company_purchase.append(p)
        paginator = Paginator(company_purchase, 5) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if company_purchase:
            messages.success(request, f'د {search_value} لپاره معلومات پیدا سول!')
        else:
            messages.warning(request, 'غوښتل سوي معلومات شتون نه لري!')
        return render(request, 'medicine/company_purchase/list_company_purchase.html', {'page_obj':page_obj, 'search_value':search_value})
    else:
        return redirect('page_404')
# COMPANY PURCHASE VIEWS END