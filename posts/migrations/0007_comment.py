# Generated by Django 4.2 on 2023-04-24 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.products')),
            ],
        ),
    ]
