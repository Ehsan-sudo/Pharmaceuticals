from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=15, null=True)
    location = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100, null=True)
    debt = models.FloatField(default=0)

    def __str__(self):
        return self.name


class CustomerPurchase(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='purchases')
    date = models.DateField(auto_now_add=True)


class CustomerPurchaseMedicine(models.Model):
    purchase = models.ForeignKey('CustomerPurchase', on_delete=models.CASCADE, related_name='medicines')
    medicine = models.ForeignKey('Medicine', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.FloatField()


class CompanyPurchase(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='purchases')
    date = models.DateField(auto_now_add=True)


class CompanyPurchaseMedicine(models.Model):
    purchase = models.ForeignKey('CompanyPurchase', on_delete=models.CASCADE, related_name='medicines')
    medicine = models.ForeignKey('Medicine', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.FloatField()


class CustomerPayment(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='payments')
    date = models.DateField(auto_now_add=True)
    payed_amount = models.FloatField()


class MedicineType(models.Model):
    type = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.type
    

class Medicine(models.Model):
    brand_name = models.CharField(max_length=100, unique=True)
    medical_name = models.CharField(max_length=100, null=True)
    formula = models.TextField(max_length=300, null=True)
    type = models.ForeignKey('MedicineType', on_delete=models.CASCADE, related_name='medicines')
    expire_date = models.DateField()
    in_price = models.FloatField()
    out_price = models.FloatField(null=True)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='medicine/img/', default='medicine/img/default.jpg', null=True)

    def __str__(self):
        return self.brand_name
        
