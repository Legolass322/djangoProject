from django.db import models


class Product(models.Model):
    name = models.CharField('Имя', max_length = 70)
    description = models.TextField('Описание', max_length = 500)
    price = models.CharField('Цена', max_length = 20)
    img = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name

    def get_price_rub(self):
        tmp = self.price.split()
        return int(tmp[0]) + int(tmp[2]) / 100