# Zacklyのフォーム関係
from django import forms
from .models import Income, FixedCost, SpFixedCost

#収入記入欄１個目
class incomeFormAdd(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['item1','amountOfIncome1']

# 収入記入欄２個目
class incomeFormAdd2(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['item2','amountOfIncome2']

# 収入記入欄３個目
class incomeFormAdd3(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['item3','amountOfIncome3']

# 収入記入欄４個目
class incomeFormAdd4(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['item4','amountOfIncome4']

#固定費の記入欄１個目-------------------------------------------------
class fixedCostFormAdd(forms.ModelForm):
    class Meta:
        model = FixedCost
        fields = ['item1','amountOfFixedCost1']

class fixedCostFormAdd2(forms.ModelForm):
    class Meta:
        model = FixedCost
        fields = ['item2','amountOfFixedCost2']

# 特別支出----------------------------------------------------------
class SpFixedCostFormsAdd(forms.ModelForm):
    class Meta:
        model = SpFixedCost
        fields = ['item','amountOfSpFixedCost']