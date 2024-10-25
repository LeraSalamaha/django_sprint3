"""Views функция для blog."""
from django.shortcuts import render, get_object_or_404

from .models import Category
from .utils import get_published_posts

LIMIT_POSTS_COUNT = 5


def index(request):
    """Views функция для главной страницы."""
    post_list = get_published_posts()[:LIMIT_POSTS_COUNT]

    context = {
        'post_list': post_list,
    }

    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """Views функция для детализации постов."""
    post = get_object_or_404(get_published_posts(), pk=post_id)

    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Views функция для выводов постов выбранной категории."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True)

    post_list = get_published_posts().filter(category=category)

    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, 'blog/category.html', context)
