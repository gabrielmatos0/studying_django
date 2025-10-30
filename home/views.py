from django.shortcuts import render

def home(request):
    print('cliente acessou a página principal')
    return render(request, 'home/index.html')
