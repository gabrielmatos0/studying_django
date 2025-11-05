from django.shortcuts import render

def blog(request):
    print('cliente acessou a página de blog')

    context = {
        'text': 'Página de Blog!',
        'title': 'Blog - '
    }

    return render(request, 'blog/index.html', context)


def exemplo(request):
    print('cliente acessou a página de exemplo')

    context = {
        'text': 'EXEMPLO',
        'title': 'EXEMPLO - '
    }

    return render(request, 'blog/exemplo.html', context)
