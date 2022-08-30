from medicine.models import *
from django.shortcuts import render, redirect
from django.contrib import messages


def remaining_debt_report(request):
    return render(request, 'medicine/report/remaining_debt_report.html')
