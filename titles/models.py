from django.db import models
from django.core.validators import MaxValueValidator
import datetime

now = datetime.datetime.now()


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', unique=True,
                            max_length=200,)
    slug = models.SlugField(verbose_name='Слаг категории', unique=True,)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Genre(models.Model):
    name = models.CharField(verbose_name='Название жанра', unique=True,
                            max_length=200,)
    slug = models.SlugField(verbose_name='Слаг жанра', unique=True,)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Title(models.Model):
    name = models.CharField(verbose_name='Название произведения',
                            max_length=200)
    year = models.PositiveIntegerField(
        verbose_name='Год произведения',
        validators=(MaxValueValidator(now.year),),
        db_index=True)
    rating = models.FloatField(verbose_name='Рейтинг произведения',
                               blank=True, null=True)
    description = models.TextField(verbose_name='Описание произведения', )
    category = models.ForeignKey(Category, blank=True, null=True,
                                 on_delete=models.SET_NULL,
                                 related_name='categories')
    genre = models.ManyToManyField(Genre, related_name='genres')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
