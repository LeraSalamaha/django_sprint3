"""Views функция для blog."""
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Category


def index(request):
    """Views функция для главной страницы."""
    template_name = 'blog/index.html'

    now = timezone.now()

    post_list = Post.objects.all().filter(
        is_published=True, pub_date__lte=now,
        category__is_published=True)[:5]

    context = {
        'post_list': post_list,
    }

    return render(request, template_name, context)


def post_detail(request, id):
    """Views функция для детализации постов."""
    template_name = 'blog/detail.html'
    now = timezone.now()

    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            pub_date__lte=now,
            category__is_published=True),
        pk=id
    )
    context = {
        'post': post,
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    """Views функция для выводов постов выбранной категории."""
    template_name = 'blog/category.html'

    category = get_object_or_404(Category, slug=category_slug)

    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    )

    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, template_name, context)
