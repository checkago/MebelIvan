import datetime

from django.db import models


class Banner(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='media/banners', verbose_name='Изображение')
    date = models.DateField(default=datetime.date.today, verbose_name='Дата создания')
    end_date = models.DateField(blank=True, verbose_name='Дата окончания публикации')
    text = models.CharField(max_length=150, verbose_name='Текст баннера')
    additional_text = models.CharField(max_length=150, verbose_name='Доп. текст')
    link = models.URLField(verbose_name='Ссылка', blank=True)

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'

    def __str__(self):
        return self.name


class
