# Generated by Django 4.1.7 on 2023-06-24 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
    ]
