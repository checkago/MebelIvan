# Generated by Django 5.0.2 on 2024-03-02 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mebel_app', '0007_position_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/employee', verbose_name='Фото'),
        ),
    ]
