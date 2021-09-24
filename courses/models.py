from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=90, verbose_name="عنوان")
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="استاد")
    create_date = models.DateField(auto_now=True, verbose_name="زمان ایجاد")
    price = models.IntegerField(verbose_name="قیمت", default=0)
    updated_date = models.DateField(
        auto_now=True, verbose_name="زمان آخرین آپدیت")
    description = models.TextField(verbose_name="توضیحات")
    photo = models.ImageField(upload_to="media/course_images", verbose_name='عکس', null=True, blank=True)

    class Meta:
        verbose_name = "آموزش"
        verbose_name_plural = "آموزش ها "

    def __str__(self):
        return self.title


class Session(models.Model):
    title = models.CharField(max_length=90, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="نام آموزش")
    video = models.FileField(
        upload_to="media/course_videos", verbose_name="ویدئو")
    time = models.IntegerField(default=0, verbose_name="مدت زمان ویدئو")

    class Meta:
        verbose_name = "قسمت"
        verbose_name_plural = "قسمت ها"

    def __str__(self):
        return self.title
