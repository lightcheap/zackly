
from django.db import models

# Create your models here.
class Income(models.Model):
    """収入"""
    #収入の項目はひとまず4セット

    #item = 収入の名目
    item1 = models.CharField(verbose_name = '品目', max_length=30, default = " ", blank = True, null = True, )
    #amountOfIncome = 収入の金額    
    amountOfIncome1 = models.IntegerField(verbose_name = '収入', default = 0, blank = True, null = True)
    #precisely = 金額が正確かどうか(ざっくりー or NOTざっくりー)
    ZACKLY = 'za'
    NOTZACKLY = 'nz'
    PRECISELY1 = ((ZACKLY, 'zackly'),(NOTZACKLY, 'notZackly'),)
    precisely1 = models.CharField(max_length = 2, choices = PRECISELY1, default = ZACKLY,)

    item2 = models.CharField(verbose_name = '品目', max_length=30, default = " ", blank = True, null = True)
    amountOfIncome2 = models.IntegerField(verbose_name = '収入', default = 0, blank = True, null = True)
    item3 = models.CharField(verbose_name = '品目', max_length=30, default = " ", blank = True, null = True)
    amountOfIncome3 = models.IntegerField(verbose_name = '収入', default = 0, blank = True, null = True)
    item4 = models.CharField(verbose_name = '品目', max_length=30, default = " ", blank = True, null = True)
    amountOfIncome4 = models.IntegerField(verbose_name = '収入', default = 0, blank = True, null = True)
    def __str__(self):
        return self.item1, self.amountOfIncome1, self.precisely1, self.item2, self.item3, self.item4, 


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
