
from django.db import models

# Create your models here.
class Income(models.Model):
    """収入"""
    #収入の項目はひとまず4セット
    #1セット目
    #item = 収入の名目
    item1 = models.CharField(verbose_name = '品目', max_length=30, default = " ", blank = True, null = True, )
    #amountOfIncome = 収入の金額    
    amountOfIncome1 = models.IntegerField(verbose_name = '収入', default = 0, blank = True, null = True)
    #precisely = 金額が正確かどうか(ざっくりー or NOTざっくりー)
    ZACKLY = 'za'
    NOTZACKLY = 'nz'
    PRECISELY1 = ((ZACKLY, 'zackly'),(NOTZACKLY, 'notZackly'),)
    precisely1 = models.CharField(max_length = 2, choices = PRECISELY1, default = ZACKLY,)
    #2セット目
    item2 = models.CharField(verbose_name = '品目', max_length=30, default = " ", blank = True, null = True)
    amountOfIncome2 = models.IntegerField(verbose_name = '収入', default = 0, blank = True, null = True)
    #3セット目
    item3 = models.CharField(verbose_name = '品目', max_length=30, default = " ", blank = True, null = True)
    amountOfIncome3 = models.IntegerField(verbose_name = '収入', default = 0, blank = True, null = True)
    #4セット目
    item4 = models.CharField(verbose_name = '品目', max_length=30, default = " ", blank = True, null = True)
    amountOfIncome4 = models.IntegerField(verbose_name = '収入', default = 0, blank = True, null = True)
    def __str__(self):
        return self.item1, self.amountOfIncome1, self.precisely1, self.item2, self.item3, self.item4, 


class FixedCost(models.Model):
    """固定費"""
    # 固定費は10セットくらい
    #　1セット目
    item1 = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost1 = models.IntegerField(verbose_name = '固定', default = 0, blank = True, null = True)
    #　2セット目
    item2 = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost2 = models.IntegerField(verbose_name = '固定', default = 0, blank = True, null = True)
    #　3セット目
    item3 = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost3 = models.IntegerField(verbose_name = '固定', default = 0, blank = True, null = True)
    #　4セット目
    item4 = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost4 = models.IntegerField(verbose_name = '固定', default = 0, blank = True, null = True)
    #　5セット目
    item5 = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost5 = models.IntegerField(verbose_name = '固定', default = 0, blank = True, null = True)


    def __str__(self):
        return self.item1


class SpFixedCost(models.Model):
    """特別費"""
    item = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True)
    amountOfSpFixedCost = models.IntegerField(verbose_name = '特別', default = 0, blank = True, null = True)

    def __str__(self):
        return self.item
