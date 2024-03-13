# Generated by Django 5.0.2 on 2024-03-02 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mebel_app', '0011_gallery_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='icon',
        ),
        migrations.AddField(
            model_name='social',
            name='icon',
            field=models.CharField(default=1, max_length=50, verbose_name='Тег иконки'),
            preserve_default=False,
        ),
    ]
