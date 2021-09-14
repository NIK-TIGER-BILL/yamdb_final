from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from users.models import User
from titles.models import Title


class Review(models.Model):
    title_id = models.ForeignKey(Title,
                                 on_delete=models.CASCADE,
                                 verbose_name='Произведение',
                                 related_name='review',
                                 null=True)
    text = models.TextField(max_length=2000,
                            verbose_name='Отзыв')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='review',
                               verbose_name='Пользователь')
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='Оценка'
    )
    pub_date = models.DateTimeField('date published',
                                    auto_now_add=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Review'

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    review_id = models.ForeignKey(Review,
                                  on_delete=models.CASCADE,
                                  verbose_name='Отзыв',
                                  related_name='comments',
                                  null=True)
    text = models.CharField(max_length=1000,
                            verbose_name='Комментарий')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='Пользователь',
                               null=True)
    pub_date = models.DateTimeField('date published',
                                    auto_now_add=True)

    class Meta:
        ordering = ['id']
