# Generated by Django 5.0.2 on 2024-03-01 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mebel_app', '0002_about_contact_gallerycategory_project_gallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallerycategory',
            options={'verbose_name': 'Категория изображения услуг', 'verbose_name_plural': 'Категории изображений услуг'},
        ),
    ]