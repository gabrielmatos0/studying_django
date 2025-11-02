from django.shortcuts import render

def home(request):
    print('cliente acessou a página principal')
    context = {
        'text': 'Página de Home!',
        'title': 'Home - '
    }

    return render(
        request,
        'home/index.html',
        context
    )
