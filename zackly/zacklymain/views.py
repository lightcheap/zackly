from django.shortcuts import render, redirect # テンプレートのレンダリングで使う
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.views import View # 基本汎用クラスビューで使う
from .forms import incomeFormAdd # 定義したフォーム
from .models import Income # 定義したモデル


class top(View):
    def get(self, request, *args, **kwargs):
        d ={
            'hour':datetime.now(),
        }    
        #template = loader.get_template('zacklymain/toppage.html')
        return render(request,'zacklymain/toppage.html', d)

class main(View):
    def get(self, request, *args, **kwargs):
        d = {
            'month':datetime.now().month,
            'income':request.GET.get('income-sample'),
        }
        #template = loader.get_template('zacklymain/main.html')
        return render(request,'zacklymain/main.html', d)

class history(View):
    def get(self, request, *args, **kwargs):
        income = Income.objects.values('item','amountOfIncome')
        d = {
            'income': income,
        }

        #template = loader.get_template('zacklymain/history.html')
        return render(request,'zacklymain/history.html', d)

class edit(View):
    def get(self, request, *args, **kwargs):

        return render(request,'zacklymain/edit.html')
        
def create(request):
    # IncomeのModelを作成する
    member = Income()

    # Postの時
    if request.method == 'POST':
        # フォーム生成
        
        form = incomeFormAdd( request.POST, instance = member)

        if form.is_valid(): #バリデーションがOKなら保存する
            member = form.save(commit = False)
            member.save()
            return redirect('/history')

    else:
        form = incomeFormAdd( request.POST, instance = obj)

    
    return render(request,'zacklymain/edit.html', dict(form=form) )
