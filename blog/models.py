from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)        # Поле для заголовка
    content = models.TextField()                    # Поле для текста статьи
    pub_date = models.DateTimeField(auto_now_add=True)  # Публикация даты/времени создания

    def __str__(self):
        return self.title  # Для красивого отображения в админке