from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404


# Create your views here.


def home(request):
   return render(request, 'portfolio/home.html',
                 {'portfolio': home})


def login(request):
   return render(request, 'portfolio/login.html',
                 {'portfolio': login})


def department_view(request,pk):
    department= get_object_or_404(Department,pk=pk)
    deoartment = Department.objects.filter()
    customers = Customer.objects.filter(created_date__lte=timezone.now())
    investments =Investment.objects.filter(customer=pk)
    return render(request,'hackpracs/department.html')
