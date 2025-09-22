# blog/urls.py

from django.urls import path
from . import views  # импортируем views из текущего каталога

urlpatterns = [
    path('', views.article_list, name='article_list'), # меняем hello_world на article_list
]