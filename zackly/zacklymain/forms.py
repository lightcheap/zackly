# Zacklyのフォーム関係
from django import forms
from .models import Income

class incomeFormAdd(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['income','amountOfIncome']