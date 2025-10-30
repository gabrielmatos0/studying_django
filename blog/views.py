from django.shortcuts import render

def blog(request):
    print('cliente acessou a página de blog')
    return render(request, 'blog/index.html')

def exemplo(request):
    print('cliente acessou a página de exemplo')
    return render(request, 'blog/exemplo.html')
