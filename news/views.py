from django.shortcuts import render
from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-title',
    template_name = 'PostCategory.html'
    context_object_name ='PostCategory'


class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'PostCategoryOneByOne.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'PostCategory'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context


