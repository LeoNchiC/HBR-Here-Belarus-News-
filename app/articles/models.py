import datetime
from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length=200)
    article_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.article_title if hasattr(self, 'article_title' ) else "no title"

    def was_pub_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField('Имя автора', max_length=50)
    comment_text = models.CharField('Текст комментария', max_length=1000)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Image(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')
    image_article = models.ImageField('Изображение к статье', height_field='image_height', width_field='image_width')
    image_height = models.SmallIntegerField(default=200)
    image_width = models.SmallIntegerField(default=200)

    def __str__(self):
        return f"{self.article}"

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
