from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    # return HttpResponse('ciaooo')
    return render(request, 'primapp/home.html',{'nome':'Davide'})

def password(request):
    
    caratteri = list('abcdefghilmnopqrstuvz')
    lunghezza = int(request.GET.get('lunghezza',8))
    pwd = ''
    if request.GET.get('uppercase'):
        caratteri.extend('ABCDEFGHILMNOPQRSTUVZ')
    
    if request.GET.get('special'):
        caratteri.extend('@#$%&^')
    
    if request.GET.get('numbers'):
        caratteri.extend('0123456789')

    for x in range (lunghezza):
        pwd += random.choice(caratteri)

    return render(request, 'primapp/password.html', {'password':pwd})

def about(request):
    # return HttpResponse('ciaooo')
    return render(request, 'primapp/about.html')