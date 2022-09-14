from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    TYPES = [
        ('tank', 'Танки'),
        ('healer', 'Хилы'),
        ('DD', 'ДД'),
        ('merchant', 'Торговцы'),
        ('gildmaster', 'Гилдмастеры'),
        ('questgiver', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potionmaker', 'Зельевары'),
        ('spellmaster', 'Мастера заклинаний'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    datecreation = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    type = models.CharField(max_length=16, choices=TYPES, default='merchant', verbose_name='Тип обьявления')
    content = RichTextField(blank=True, null=True, verbose_name='Сообщение')

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text}'

