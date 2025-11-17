from django.shortcuts import render
from blog.data import posts
from typing import Any
from django.http import HttpRequest, HttpResponse


def blog(request):
    print('cliente acessou a página de blog')

    context = {
        'text': 'Página de Blog!',
        'title': 'Blog - ',
        'posts': posts
    }

    return render(request, 'blog/index.html', context)


def post(request: HttpRequest, post_id: int) -> HttpResponse:
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Exception('Post inexistente.')

    context = {
        # 'text': 'Página de Post!',
        'title': found_post['title'] + ' - ',
        'post': found_post
    }

    return render(request, 'blog/post.html', context)


def exemplo(request):
    print('cliente acessou a página de exemplo')

    context = {
        'text': 'EXEMPLO',
        'title': 'EXEMPLO - '
    }

    return render(request, 'blog/exemplo.html', context)
