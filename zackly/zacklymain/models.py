
from django.db import models

# Create your models here.
class Income(models.Model):
    """収入"""
    item = models.CharField(verbose_name = '品目', max_length=30, default = " ", blank = True, null = True)
    amountOfIncome = models.IntegerField(verbose_name = '収入', default = 0, blank = True, null = True)

    def __str__(self):
        return self.item   


class FixedCost(models.Model):
    """固定費"""
    item = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost = models.IntegerField(verbose_name = '固定', default = 0, blank = True, null = True)

    def __str__(self):
        return self.item


class SpFixedCost(models.Model):
    """特別費"""
    item = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True)
    amountOfSpFixedCost = models.IntegerField(verbose_name = '特別', default = 0, blank = True, null = True)

    def __str__(self):
        return self.item
