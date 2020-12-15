from django.shortcuts import render
from django.http import HttpResponse
import random


def password_generator_home(request):
    return render(request, 'generator/home.html')


def password_generated(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!#+*><-_/(){}[]%&$§€'))

    length = int(request.GET.get('length'))

    generated_password = ''

    for i in range(length):
        generated_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': generated_password})
