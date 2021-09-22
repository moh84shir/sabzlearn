from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    subject = models.CharField(max_length=120, verbose_name='موضوع')
    email = models.EmailField(verbose_name='ایمیل')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='کاربر')
    text = models.TextField(verbose_name='متن')
    is_read = models.BooleanField(
        default=False, verbose_name='خوانده شده/نشده')

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'

    def __str__(self):
        return self.title
