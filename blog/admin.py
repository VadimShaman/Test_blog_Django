from django.contrib import admin
from .models import Article  # импортируем нашу модель

admin.site.register(Article) # регистрируем ее в админке