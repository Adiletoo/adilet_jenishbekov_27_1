# Generated by Django 4.2 on 2023-04-18 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_products_image_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]