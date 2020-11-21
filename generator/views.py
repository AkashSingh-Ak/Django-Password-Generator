from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def hello(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    character = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        character.extend(list('1234567890'))
    
    if request.GET.get('special'):
        character.extend(list('@#$%&'))

    len = int(request.GET.get('length',12))
    thepass=''
    for x in range(len):
        thepass += random.choice(character)
    return render(request, 'generator/password.html', {'password': thepass})


