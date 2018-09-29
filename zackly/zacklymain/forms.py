# Zacklyのフォーム関係
from django import forms
from zacklymain.models import balanceOfPayment

#収入記入欄１個目
class incomeFormAdd(forms.ModelForm):
    class Meta:
        model = balanceOfPayment
        fields = ['incomeName1','amountOfIncome1','incomeName2','amountOfIncome2',
        'incomeName3','amountOfIncome3','incomeName4','amountOfIncome4']


#固定費の記入欄１個目-------------------------------------------------
class fixedCostFormAdd(forms.ModelForm):
    class Meta:
        model = balanceOfPayment
        fields = ['fixedCostName1','amountOfFixedCost1','fixedCostName2','amountOfFixedCost2',
        'fixedCostName3','amountOfFixedCost3','fixedCostName4','amountOfFixedCost4']


# 特別支出----------------------------------------------------------
class SpFixedCostFormsAdd(forms.ModelForm):
    class Meta:
        model = balanceOfPayment
        fields = ['spFixedCostName1','amountOfSpFixedCost1','spFixedCostName2','amountOfSpFixedCost2',
        'spFixedCostName3','amountOfSpFixedCost3','spFixedCostName4','amountOfSpFixedCost4']

        