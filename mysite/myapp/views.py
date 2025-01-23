from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def book_post(request):
    post = Post.objects.all()
    context = {
        'books': post
    }

    return render(request, 'index.html', context)