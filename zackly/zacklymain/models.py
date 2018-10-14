
from django.db import models
from django.utils import timezone

# Create your models here.
class balanceOfPayment(models.Model):
    """収入、固定費、特別費をまとめた"""
    #収入の項目は4セット
    #incomeName = 収入の名目　/　amountOfIncome = 収入の金額
    #precisely = 金額が正確かどうか(ざっくりー or NOTざっくりー)

    createdAt = models.DateTimeField(
        verbose_name = '登録日',
        default= timezone.now,
        auto_now =False, #モデルインスタンスを保存するたびに更新するかどうか
        auto_now_add=False, #DBにINSERTされるたびに更新するかどうか
        )

    updatedAt = models.DateTimeField(
        verbose_name = '更新日',
        auto_now_add=True,
        blank = True,
        null = True
        )

    year = models.IntegerField(
        #何年のデータか　とりあえずblank、nullは入れてるけどあとで削除
        verbose_name = '年',
        blank = True,
        null = True
        )

    month = models.IntegerField(
        #何月のデータか　とりあえずblank、nullは入れてるけどあとで削除
        verbose_name = '月',
        blank = True,
        null = True
        )
    
    incomeName1 = models.CharField(
        verbose_name = '収入名1',
        max_length=30, #最大文字数
        default = " ", #デフォルトで入るデータ
        blank = True,
        null = True,
        )

    amountOfIncome1 = models.IntegerField(
        verbose_name = '収入金額1',
        default = 0,
        blank = True,
        null = True
        )
    #----ざっくりかきっちりかの判定とかするデータモデル----
    ZACKLY = 'za'
    NOTZACKLY = 'nz'
    PRECISELY1 = ((ZACKLY, 'zackly'),(NOTZACKLY, 'notZackly'),)

    precisely1 = models.CharField( 
        max_length = 2,
        choices = PRECISELY1,
        default = ZACKLY,
        )

    #-----------------------------------------------------------
    incomeName2 = models.CharField(verbose_name = '収入名2', max_length=30, default = " ", blank = True, null = True)
    amountOfIncome2 = models.IntegerField(verbose_name = '収入金額2', default = 0, blank = True, null = True)
    #-----------------------------------------------------------
    incomeName3 = models.CharField(verbose_name = '収入名3', max_length=30, default = " ", blank = True, null = True)
    amountOfIncome3 = models.IntegerField(verbose_name = '収入金額3', default = 0, blank = True, null = True)
    #-----------------------------------------------------------
    incomeName4 = models.CharField(verbose_name = '収入名4', max_length=30, default = " ", blank = True, null = True)
    amountOfIncome4 = models.IntegerField(verbose_name = '収入金額4', default = 0, blank = True, null = True)
    ####################################
    # 固定費は10セットくらい
    # 金額が正確かどうかの項目も作るよ

    fixedCostName1 = models.CharField(
        verbose_name = '固定費名1',
        max_length = 30,
        default = " ",
        blank = True,
        null = True
        )

    amountOfFixedCost1 = models.IntegerField(
        verbose_name = '固定費金額1',
        default = 0,
        blank = True,
        null = True
        )

    #-----------------------------------------------------------
    fixedCostName2 = models.CharField(verbose_name = '固定費名2', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost2 = models.IntegerField(verbose_name = '固定費金額2', default = 0, blank = True, null = True)
    #-----------------------------------------------------------
    fixedCostName3 = models.CharField(verbose_name = '固定費名3', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost3 = models.IntegerField(verbose_name = '固定費金額3', default = 0, blank = True, null = True)
    #-----------------------------------------------------------
    fixedCostName4 = models.CharField(verbose_name = '固定費名4', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost4 = models.IntegerField(verbose_name = '固定費金額4', default = 0, blank = True, null = True)
    #-----------------------------------------------------------
    fixedCostName5 = models.CharField(verbose_name = '固定費名5', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost5 = models.IntegerField(verbose_name = '固定費金額5', default = 0, blank = True, null = True)
    #-----------------------------------------------------------
    fixedCostName6 = models.CharField(verbose_name = '固定費名6', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost6 = models.IntegerField(verbose_name = '固定費金額6', default = 0, blank = True, null = True)
    #-----------------------------------------------------------
    fixedCostName7 = models.CharField(verbose_name = '固定費名7', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost7 = models.IntegerField(verbose_name = '固定費金額7', default = 0, blank = True, null = True)
    #-----------------------------------------------------------
    fixedCostName8 = models.CharField(verbose_name = '固定費名8', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost8 = models.IntegerField(verbose_name = '固定費金額8', default = 0, blank = True, null = True)
    #-----------------------------------------------------------
    fixedCostName9 = models.CharField(verbose_name = '固定費名9', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost9 = models.IntegerField(verbose_name = '固定費金額9', default = 0, blank = True, null = True)
    #-----------------------------------------------------------
    fixedCostName10 = models.CharField(verbose_name = '固定費名10', max_length = 30, default = " ", blank = True, null = True)
    amountOfFixedCost10 = models.IntegerField(verbose_name = '固定費金額10', default = 0, blank = True, null = True)

    ###############################################
    # 特別費
    # spFixedCostName = 特別費名　amountOfSpFixedCost = 特別費の金額
    # 金額が正確かどうかの項目も作るよ

    spFixedCostName1 = models.CharField(
        verbose_name = '特別費1',
        max_length = 30,
        default = " ",
        blank = True,
        null = True
        )

    amountOfSpFixedCost1 = models.IntegerField(
        verbose_name = '特別費金額1',
        default = 0,
        blank = True,
        null = True
        )

    #----------------------------------------------
    spFixedCostName2 = models.CharField(verbose_name = '特別費2', max_length = 30, default = " ", blank = True, null = True) 
    amountOfSpFixedCost2 = models.IntegerField(verbose_name = '特別費金額2', default = 0, blank = True, null = True)
    #----------------------------------------------
    spFixedCostName3 = models.CharField(verbose_name = '特別費3', max_length = 30, default = " ", blank = True, null = True) 
    amountOfSpFixedCost3 = models.IntegerField(verbose_name = '特別費金額3', default = 0, blank = True, null = True)
    #----------------------------------------------
    spFixedCostName4 = models.CharField(verbose_name = '特別費4', max_length = 30, default = " ", blank = True, null = True) 
    amountOfSpFixedCost4 = models.IntegerField(verbose_name = '特別費金額4', default = 0, blank = True, null = True)
    #----------------------------------------------
    spFixedCostName5 = models.CharField(verbose_name = '特別費5', max_length = 30, default = " ", blank = True, null = True) 
    amountOfSpFixedCost5 = models.IntegerField(verbose_name = '特別費金額5', default = 0, blank = True, null = True)
    #----------------------------------------------
    def __str__(self):
        return str(self.month)
