from django.http import HttpResponse
# from django.shortcuts import render

def home(request):
    print('cliente acessou a página principal')
    return HttpResponse('Página principal')
