from django.shortcuts import render
from blog.data import posts


def blog(request):
    print('cliente acessou a página de blog')

    context = {
        'text': 'Página de Blog!',
        'title': 'Blog - ',
        'posts': posts
    }

    return render(request, 'blog/index.html', context)


def post(request, id):
    print('post id:', id)

    context = {
        'text': 'Página de Post!',
        'title': 'Post - ',
        'posts': posts
    }

    return render(request, 'blog/index.html', context)


def exemplo(request):
    print('cliente acessou a página de exemplo')

    context = {
        'text': 'EXEMPLO',
        'title': 'EXEMPLO - '
    }

    return render(request, 'blog/exemplo.html', context)
