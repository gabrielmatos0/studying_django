from django.http import HttpResponse
# from django.shortcuts import render

def blog(request):
    print('cliente acessou a página de blog')
    return HttpResponse('Meu Blog')

def exemplo(request):
    print('cliente acessou a página de exemplo')
    return HttpResponse('Meu exemplo')
