from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def data_input(request):
    return render(request, 'data_input.html')
