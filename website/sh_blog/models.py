from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from precise_bbcode import fields

def user_media_path(instance, filename):
    return 'user_{}/{}'.format(instance.author.id, filename)

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES= (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = fields.BBCodeTextField(verbose_name='Описание')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    rubric = models.ForeignKey('Rubric', on_delete=models.PROTECT, null=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    fixed = models.BooleanField(default=False)
    image = models.ImageField(upload_to=user_media_path, null=True)

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

class Rubric(models.Model):

    name = models.CharField(max_length=250)
    image = models.CharField(max_length=250, null=True)

    class Meta:
        verbose_name = "Рубрика"
        verbose_name_plural = "Рубрики"
        ordering = ('name',)

    def __str__(self):
        return self.name

