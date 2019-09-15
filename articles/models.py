from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    paid_subscription = models.BooleanField(default=False, verbose_name='Оформлена платная подписка')


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    image = models.ImageField(upload_to='static/image', verbose_name='Тематическое изображение статьи')
    text = models.TextField(verbose_name='Статья')
    paid_article = models.BooleanField(default=False, verbose_name='Платная статья')
