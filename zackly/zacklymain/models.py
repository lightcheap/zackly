
from django.db import models

# Create your models here.
class balanceOfPayment(models.Model):
    """収入、固定費、特別費をまとめた"""
    #収入の項目は4セット
    #incomeName = 収入の名目　/　amountOfIncome = 収入の金額
    #precisely = 金額が正確かどうか(ざっくりー or NOTざっくりー)
    incomeName1 = models.CharField(verbose_name = '品目', max_length=30, default = " ", blank = True, null = True, )
    amountOfIncome1 = models.IntegerField(verbose_name = '収入', default = 0, blank = True, null = True)
    ZACKLY = 'za'
    NOTZACKLY = 'nz'
    PRECISELY1 = ((ZACKLY, 'zackly'),(NOTZACKLY, 'notZackly'),)
    precisely1 = models.CharField(max_length = 2, choices = PRECISELY1, default = ZACKLY,)
    #-----------------------------------------------------------
    incomeName2 = models.CharField(verbose_name = '品目', max_length=30, default = " ", blank = True, null = True)
    amountOfIncome2 = models.IntegerField(verbose_name = '収入', default = 0, blank = True, null = True)
    #-----------------------------------------------------------
    incomeName3 = models.CharField(verbose_name = '品目', max_length=30, default = " ", blank = True, null = True)
    amountOfIncome3 = models.IntegerField(verbose_name = '収入', default = 0, blank = True, null = True)
    #-----------------------------------------------------------
    incomeName4 = models.CharField(verbose_name = '品目', max_length=30, default = " ", blank = True, null = True)
    amountOfIncome4 = models.IntegerField(verbose_name = '収入', default = 0, blank = True, null = True)
    ####################################
    # 固定費は10セットくらい
    #　fixedCostName = 固定費の項目名　/　amountOfFixedCost = 固定費の金額
    #　金額が正確かどうかの項目も作るよ
    fixedCostName1 = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost1 = models.IntegerField(verbose_name = '固定', default = 0, blank = True, null = True)
    #-----------------------------------------------------------
    fixedCostName2 = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost2 = models.IntegerField(verbose_name = '固定', default = 0, blank = True, null = True)
    #-----------------------------------------------------------
    fixedCostName3 = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost3 = models.IntegerField(verbose_name = '固定', default = 0, blank = True, null = True)
    #-----------------------------------------------------------
    fixedCostName4 = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost4 = models.IntegerField(verbose_name = '固定', default = 0, blank = True, null = True)
    #-----------------------------------------------------------
    fixedCostName5 = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost5 = models.IntegerField(verbose_name = '固定', default = 0, blank = True, null = True)
    #-----------------------------------------------------------
    fixedCostName6 = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost6 = models.IntegerField(verbose_name = '固定', default = 0, blank = True, null = True)
    #-----------------------------------------------------------
    fixedCostName7 = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost7 = models.IntegerField(verbose_name = '固定', default = 0, blank = True, null = True)
    #-----------------------------------------------------------
    fixedCostName8 = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost8 = models.IntegerField(verbose_name = '固定', default = 0, blank = True, null = True)
    #-----------------------------------------------------------
    fixedCostName9 = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost9 = models.IntegerField(verbose_name = '固定', default = 0, blank = True, null = True)
    #-----------------------------------------------------------
    fixedCostName10 = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost10 = models.IntegerField(verbose_name = '固定', default = 0, blank = True, null = True)
    ###############################################
    # 特別費
    # spFixedCostName = 特別費名　amountOfSpFixedCost = 特別費の金額
    # 金額が正確かどうかの項目も作るよ
    spFixedCostName1 = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True) 
    amountOfSpFixedCost1 = models.IntegerField(verbose_name = '特別', default = 0, blank = True, null = True)
    #----------------------------------------------
    spFixedCostName2 = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True) 
    amountOfSpFixedCost2 = models.IntegerField(verbose_name = '特別', default = 0, blank = True, null = True)
    #----------------------------------------------
    spFixedCostName3 = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True) 
    amountOfSpFixedCost3 = models.IntegerField(verbose_name = '特別', default = 0, blank = True, null = True)
    #----------------------------------------------
    spFixedCostName4 = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True) 
    amountOfSpFixedCost4 = models.IntegerField(verbose_name = '特別', default = 0, blank = True, null = True)
    #----------------------------------------------
    spFixedCostName5 = models.CharField(verbose_name = '品目', max_length = 30, default = " ", blank = True, null = True) 
    amountOfSpFixedCost5 = models.IntegerField(verbose_name = '特別', default = 0, blank = True, null = True)
    #----------------------------------------------
    def __str__(self):
        return self.incomeName1
