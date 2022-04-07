from django.shortcuts import render, redirect

from medicine.models import Company

# Create your views here.


# to find the total amount of a customer's purchase
# 
# from django.db.models import F
# customer.purchases.get(pk=1).medicines.aggregate(sum=Sum(F('unit_price')*F('quantity')))


def home(request):
    return render(request, 'medicine/home.html')


def list_company(request):
    companies = Company.objects.all()
    return render(request, 'medicine/company/list_company.html', {'companies':companies})

def add_company(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        location = request.POST.get('address')
        company = Company.objects.create(name=name, email=email, phone=phone, location=location)
        return redirect('list_company')
    return render(request, 'medicine/company/add_company.html')

def get_company(request, id):
    if Company.objects.filter(id=id).exists():
        company = Company.objects.get(pk=id)

        if request.POST:
            company.name = request.POST.get('name')
            company.email = request.POST.get('email')
            company.phone = request.POST.get('phone')
            company.location = request.POST.get('location')
            company.save()
            return redirect('list_company')
        else:
            return render(request, 'medicine/company/get_company.html', {'company':company})
    else:
        return redirect('page_404')

def delete_company(request, id):
    if Company.objects.filter(id=id).exists():
        Company.objects.get(pk=id).delete()
        return redirect('list_company')
    else:
        return redirect('page_404')


def page_404(request):
    return render(request, 'medicine/utility/pages-404.html')