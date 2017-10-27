from django.shortcuts import render

# Create your views here.


def home(request):
   return render(request, 'portfolio/home.html',
                 {'portfolio': home})


def login(request):
   return render(request, 'portfolio/login.html',
                 {'portfolio': login})
