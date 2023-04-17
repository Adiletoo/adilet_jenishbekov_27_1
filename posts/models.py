from django.db import models

# Create your models here.

class Products(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.FloatField()
    create_date = models.DateField(auto_now=True)
    modified_date = models.DateField(auto_now_add=True)