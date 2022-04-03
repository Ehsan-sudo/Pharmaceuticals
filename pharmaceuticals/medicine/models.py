from operator import mod
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
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)


class CustomerPurchaseMedicine(models.Model):
    purchase_id = models.ForeignKey('CustomerPurchase', on_delete=models.CASCADE)
    medicine_id = models.ForeignKey('Medicine', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.FloatField()


class CompanyPurchase(models.Model):
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)


class CompanyPurchaseMedicine(models.Model):
    purchase_id = models.ForeignKey('CompanyPurchase', on_delete=models.CASCADE)
    medicine_id = models.ForeignKey('Medicine', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.FloatField()


class CustomerPayment(models.Model):
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
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
    type_id = models.ForeignKey('MedicineType', on_delete=models.CASCADE)
    expire_date = models.DateField()
    unit_price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.brand_name