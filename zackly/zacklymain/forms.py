# Zacklyのフォーム関係
from django import forms
from .models import Income

class incomeFormAdd(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['item','amountOfIncome']

class NameForm(forms.Form):
    your_name = forms.CharField(label='Yourname', max_length = 100)