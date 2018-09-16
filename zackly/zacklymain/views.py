from django.shortcuts import render, redirect # テンプレートのレンダリングで使う
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.views import View # 基本汎用クラスビューで使う
from .models import Income, FixedCost, SpFixedCost # 定義したモデル
from .forms import incomeFormAdd, fixedCostFormAdd, SpFixedCostFormsAdd #定義したフォーム
from django.db.models import Avg, Sum

#　トップページ
class top(View):
    # 仮で時間を表示してる
    def get(self, request, *args, **kwargs):
        d ={
            'hour':datetime.now(),
        }    
        #template = loader.get_template('zacklymain/toppage.html')
        return render(request,'zacklymain/toppage.html', d)


#　メインページ
class main(View):
    def get(self, request, *args, **kwargs):
        amountOfIncome = Income.objects.values_list('amountOfIncome1',flat = True)
        sumOfAmount = Income.objects.aggregate(sx = Sum('amountOfIncome1')) # 収入の合計
        sumOfFixed = FixedCost.objects.aggregate(sx = Sum('amountOfFixedCost')) # 固定費の合計
        sumOfSpFixed = SpFixedCost.objects.aggregate(sx = Sum('amountOfSpFixedCost')) # 特別枠の合計
        #moneyToUse = Model.objects.aggregate(Sum(sumOfAmount - sumOfFixed - sumOfSpFixed))
        
        d = {
            'month':datetime.now().month,
            'income': amountOfIncome,
            'soa': sumOfAmount,
            'sof': sumOfFixed,
            'sosf': sumOfSpFixed,
        }
        #template = loader.get_template('zacklymain/main.html')
        return render(request,'zacklymain/main.html', d)

#　履歴ページ
class history(View):
    def get(self, request, *args, **kwargs):
        income = Income.objects.values('item1','amountOfIncome1') 
        fixedCost = FixedCost.objects.values('item','amountOfFixedCost')
        d = {
            'income': income,
            'fixedCost' : fixedCost,
        }

        #template = loader.get_template('zacklymain/history.html')
        return render(request,'zacklymain/history.html', d)

    def post(self, request, *args, **kwargs):
        income = Income.objects.values('item','amountOfIncome')
        d = {
            'income': income,
        }
        return render(request,'zacklymain/history.html', d)

#　入力ページ
class edit(View):
    
    def get(self, request, *args, **kwargs):
        # IncomeのModelを作成する
        modelIncome = Income()
        # FixedCostのModelを作成する
        modelFixedCost = FixedCost()
        # SpFixedCostのModelを作成する
        modelSpFixedCost = SpFixedCost()

        #　収入のフォームのインスタンスを作成
        incomeForm = incomeFormAdd( request.POST, instance = modelIncome)
        #　固定費のフォームのインスタンス
        fixedCostForm = fixedCostFormAdd( request.POST, instance = modelFixedCost )
        # 特別費のフォームのインスタンス
        SpFixedCostForm = SpFixedCostFormsAdd( request.POST, instance = modelSpFixedCost )

        dict = {
            'form' : incomeForm,
            'form2' : fixedCostForm,
            'form3' : SpFixedCostForm,
        }

        return render(request,'zacklymain/edit.html', dict)

    #フォーム入力の保存
    def post(self, request, *args, **kwargs):
        # IncomeのModelを作成する
        modelIncome = Income()
        # FixedCostのModelを作成する
        modelFixedCost = FixedCost()
        # SpFixedCostのModelを作成する
        modelSpFixedCost = SpFixedCost()

        # フォーム生成
        editForm = incomeFormAdd( request.POST, instance = modelIncome)
        #　固定費のフォームのインスタンス
        fixedCostForm = fixedCostFormAdd( request.POST, instance = modelFixedCost )
        # 特別費のフォームのインスタンス
        SpFixedCostForm = SpFixedCostFormsAdd( request.POST, instance = modelSpFixedCost )

        #バリデーションがOKなら保存する
        if editForm.is_valid():

            modelIncome = editForm.save(commit = False)
            modelFixedCost = fixedCostForm.save(commit = False)
            modelSpFixedCost = SpFixedCostForm.save(commit = False)

            modelIncome.save()
            modelFixedCost.save()
            modelSpFixedCost.save()

            return redirect('/main')
