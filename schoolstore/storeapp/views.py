from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


@csrf_protect
# def register(request):
#     return render(request, 'register.html')


def index(request):
    return render(request, 'index.html')


def login_page(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')

def form_page(request):
    return render(request, 'formpage.html')
