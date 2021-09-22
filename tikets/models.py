from django.db import models


class Tiket(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    subject = models.CharField(max_length=120, verbose_name='موضوع')
    text = models.TextField(verbose_name='متن')

    class Meta:
        verbose_name = 'تیکت'
        verbose_name_plural = 'تیکت ها'

    def __str__(self):
        return self.title
