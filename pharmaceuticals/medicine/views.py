from .my_views.company_views import home, list_company, add_company, get_company, delete_company, edit_company, render, search_company
from .my_views.company_purchase_views import list_company_purchase, add_company_purchase, get_company_purchase, delete_company_purchase, edit_company_purchase, search_company_purchase
from .my_views.customer_views import list_customer, add_customer, get_customer, delete_customer, edit_customer, search_customer
from .my_views.customer_purchase_views import list_customer_purchase, customer_purchase, add_customer_purchase, get_customer_purchase, delete_customer_purchase, edit_customer_purchase
from .my_views.customer_payment_views import list_customer_payment, add_customer_payment, get_customer_payment, delete_customer_payment, edit_customer_payment
from .my_views.medicine_type_views import list_medicine_type, add_medicine_type, get_medicine_type, delete_medicine_type, edit_medicine_type
from .my_views.medicine_views import list_medicine, add_medicine, get_medicine, delete_medicine, edit_medicine, search_medicine

def home(request):
    return render(request, 'medicine/home.html')

def page_404(request):
    return render(request, 'medicine/utility/pages-404.html')