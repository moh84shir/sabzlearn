from django.db import models
from courses.models import Course


class Comment(models.Model):
    text = models.TextField(verbose_name='متن')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='زمان ایجاد')
    updated = models.DateTimeField(
        auto_now_add=True, verbose_name='زمان ویرایش')
    course = models.ForeignKey(Course, models.CASCADE, verbose_name='آموزش')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظر ها'

    def __str__(self):
        return str(self.created)


class Replay(models.Model):
    text = models.TextField(verbose_name='متن')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='زمان ایجاد')
    updated = models.DateTimeField(
        auto_now_add=True, verbose_name='زمان ویرایش')
    comment = models.ForeignKey(Comment, models.CASCADE, verbose_name='نظر')

    class Meta:
        verbose_name = 'پاسخ'
        verbose_name_plural = 'پاسخ ها'

    def __str__(self):
        return str(self.comment.created)
