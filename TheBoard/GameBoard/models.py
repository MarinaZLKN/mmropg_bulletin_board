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
    content = models.TextField(verbose_name='Сообщение')
    upload = models.FileField(upload_to='uploads/', blank=True)

    def __str__(self):
        return f'{self.title}'

    def image_img(self):
        if self.image:
            return u'<a href="{0}" target="_blank"><img src="{0}"width= "100" / > < / a > '.format(self.image.url)
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text}'

