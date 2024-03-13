# Generated by Django 5.0.2 on 2024-03-02 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mebel_app', '0005_about_palax_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='add_active',
            field=models.BooleanField(default=True, verbose_name='Блок включен'),
        ),
        migrations.AddField(
            model_name='about',
            name='add_description',
            field=models.CharField(default=1, max_length=150, verbose_name='Описание призыва к действию'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='add_phone',
            field=models.CharField(default=1, max_length=19, verbose_name='Телефон призыва к действию'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='add_title',
            field=models.CharField(default=1, max_length=100, verbose_name='Заголовок призыва к действию'),
            preserve_default=False,
        ),
    ]