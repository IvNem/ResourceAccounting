from django.db import models


# Модель данных продукта
class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    amount = models.DecimalField(verbose_name='Количество', decimal_places=2, max_digits=7)
    unit = models.CharField(max_length=255, verbose_name='Единица измерения')
    price = models.DecimalField(verbose_name='Цена за у.е.', decimal_places=2, max_digits=7)
    date = models.DateField(verbose_name='Дата последнего поступления')

    def __str__(self):
        return self.title
