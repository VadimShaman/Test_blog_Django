from django.shortcuts import render
from .models import Article  # импортируем нашу модель

def article_list(request):
    articles = Article.objects.all().order_by('-pub_date')  # Получаем все статьи, сортируем по дате (новые сверху)
    return render(request, 'blog/article_list.html', {'articles': articles})
    # Функция render объединяет запрос, шаблон и контекст (данные для шаблона)
