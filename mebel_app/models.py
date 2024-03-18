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


class About(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название варианта')
    active = models.BooleanField(default=False, verbose_name='Текущий вариант')

    """Блок о нас"""
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    first_counter_name = models.CharField(max_length=100, verbose_name='Название счетчика 1')
    first_counter = models.IntegerField(default=178, verbose_name='Счетчик 1')
    first_counter_icon = models.CharField(max_length=50, verbose_name='Иконка счетчика 1')

    second_counter_name = models.CharField(max_length=100, verbose_name='Название счетчика 2')
    second_counter = models.IntegerField(default=178, verbose_name='Счетчик 2')
    second_counter_icon = models.CharField(max_length=50, verbose_name='Иконка счетчика 2')

    third_counter_name = models.CharField(max_length=100, verbose_name='Название счетчика 3')
    third_counter = models.IntegerField(default=178, verbose_name='Счетчик 3')
    third_counter_icon = models.CharField(max_length=50, verbose_name='Иконка счетчика 3')

    fourth_counter_name = models.CharField(max_length=100, verbose_name='Название счетчика 4')
    fourth_counter = models.IntegerField(default=178, verbose_name='Счетчик 4')
    fourth_counter_icon = models.CharField(max_length=50, verbose_name='Иконка счетчика 4')

    """Блок почему"""
    why_title = models.CharField(max_length=100, verbose_name='Заголовок блока почему')
    why_image = models.ImageField(upload_to='media/about', verbose_name='Изображение блока почему')
    why_description = models.TextField(verbose_name='Описание блока почему')

    reason_one_title = models.CharField(max_length=100, verbose_name='Заголовок причины 1')
    reason_one_description = models.TextField(verbose_name='Описание причины 1')
    reason_one_icon = models.CharField(max_length=50, verbose_name='Иконка причины 1')

    reason_two_title = models.CharField(max_length=100, verbose_name='Заголовок причины 2')
    reason_two_description = models.TextField(verbose_name='Описание причины 2')
    reason_two_icon = models.CharField(max_length=50, verbose_name='Иконка причины 2')

    reason_three_title = models.CharField(max_length=100, verbose_name='Заголовок причины 3')
    reason_three_description = models.TextField(verbose_name='Описание причины 3')
    reason_three_icon = models.CharField(max_length=50, verbose_name='Иконка причины 3')

    """Блок призыва к действию"""
    palax_image = models.ImageField(upload_to='media/palax', blank=True, verbose_name='Изображение паралакс')
    add_title = models.CharField(max_length=100, verbose_name='Заголовок призыва к действию')
    add_description = models.CharField(max_length=150, verbose_name='Описание призыва к действию')
    add_phone = models.CharField(max_length=19, verbose_name='Телефон призыва к действию')
    add_active = models.BooleanField(default=True, verbose_name='Блок включен')



    class Meta:
        verbose_name = 'Вариант О нас'
        verbose_name_plural = 'Варианты блока О Нас'

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя Фамилия')
    position = models.ForeignKey(Position, verbose_name='Должность', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/employee', blank=True, verbose_name='Фото')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    address = models.CharField(max_length=150, verbose_name='Адрес')
    email = models.EmailField(verbose_name='Почта')
    phone = models.CharField(max_length=18, verbose_name='Телефон')
    map_link = models.CharField(max_length=1000, verbose_name='Ссылка на карту')
    active = models.BooleanField(default=False, verbose_name='Основной')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контактная информация'

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    icon = models.CharField(max_length=150, verbose_name='Иконка')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Услуга на главной'
        verbose_name_plural = 'Услуги на главной'

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    image = models.ImageField(upload_to='media/projects', verbose_name='Изображение')
    short_description = models.CharField(max_length=250, verbose_name='Краткое описание')
    description = models.TextField(verbose_name='Описание')
    price = models.CharField(max_length=50, verbose_name='Стоимость')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


class GalleryCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наимевание')

    class Meta:
        verbose_name = 'Категория изображения услуг'
        verbose_name_plural = 'Категории изображений услуг'

    def __str__(self):
        return self.name


class Gallery(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, verbose_name='Категоория изображений')
    image = models.ImageField(upload_to='media/galleries', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение услуги'
        verbose_name_plural = 'Изображения услуг'

    def __str__(self):
        return self.category.name


class Social(models.Model):
    name = models.CharField(max_length=25, verbose_name='Название')
    link = models.URLField(verbose_name='Ссылка')
    icon = models.CharField(max_length=50, verbose_name='Тег иконки')

    class Meta:
        verbose_name = 'Соц. сеть'
        verbose_name_plural = 'Соц. сети'

    def __str__(self):
        return self.name






