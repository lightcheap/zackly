# Zacklyのフォーム関係
from django import forms
from .models import Income, FixedCost, SpFixedCost

class incomeFormAdd(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['item1','amountOfIncome1']


class fixedCostFormAdd(forms.ModelForm):
    class Meta:
        model = FixedCost
        fields = ['item','amountOfFixedCost']
        

class SpFixedCostFormsAdd(forms.ModelForm):
    class Meta:
        model = SpFixedCost
        fields = ['item','amountOfSpFixedCost']