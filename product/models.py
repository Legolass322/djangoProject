import os
from django.conf import settings
from django.db import models


class Product(models.Model):
    name = models.CharField('Имя', max_length = 70)
    description = models.TextField('Описание', max_length = 500)
    price = models.CharField('Цена', max_length = 20)
    img = models.ImageField(upload_to = 'images/', null = True)
    
    def __str__(self):
        return self.name