from django.shortcuts import render, redirect # テンプレートのレンダリングで使う
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.views import View # 基本汎用クラスビューで使う
from zacklymain.models import balanceOfPayment # 定義したモデル
#定義したフォーム
from zacklymain.forms import incomeFormAdd, fixedCostFormAdd, SpFixedCostFormsAdd
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
        # 収入の合計
        sx1 = Sum('amountOfIncome1') + Sum('amountOfIncome2') + Sum('amountOfIncome3') + Sum('amountOfIncome4')
        # 固定費の合計
        sx2 = Sum('amountOfFixedCost1') + Sum('amountOfFixedCost2') + Sum('amountOfFixedCost3') + Sum('amountOfFixedCost4')
        # 特別枠の合計
        sx3 = Sum('amountOfSpFixedCost1') + Sum('amountOfSpFixedCost2') + Sum('amountOfSpFixedCost3') + Sum('amountOfSpFixedCost4')
        amountOfIncome = balanceOfPayment.objects.aggregate(sx = sx1 - sx2 - sx3 )
        sumOfAmount = balanceOfPayment.objects.aggregate(sx = sx1 )
        sumOfFixed = balanceOfPayment.objects.aggregate(sx = sx2 )
        sumOfSpFixed = balanceOfPayment.objects.aggregate(sx = sx3 ) 
        
        d = {
            'month':datetime.now().month,
            'income': amountOfIncome,
            'soa': sumOfAmount,
            'sof': sumOfFixed,
            'sosf': sumOfSpFixed,
            #'mtu': moneyToUse,
        }
        #template = loader.get_template('zacklymain/main.html')
        return render(request,'zacklymain/main.html', d)

#　履歴ページ
class history(View):
    def get(self, request, *args, **kwargs):
        income = balanceOfPayment.objects.values('incomeName1','amountOfIncome1') 
        fixedCost = balanceOfPayment.objects.values('fixedCostName1','amountOfFixedCost1')
        d = {
            'income': income,
            'fixedCost' : fixedCost,
        }

        #template = loader.get_template('zacklymain/history.html')
        return render(request,'zacklymain/history.html', d)

    def post(self, request, *args, **kwargs):
        income = balanceOfPayment.objects.values('incomeName1','amountOfIncome1')
        d = {
            'income': income,
        }
        return render(request,'zacklymain/history.html', d)

#　入力ページ
class edit(View):
    
    def get(self, request, *args, **kwargs):
        # balanceOfPaymentのModelを作成する
        model = balanceOfPayment()
        #modelbop2 = balanceOfPayment()
        #modelbop3 = balanceOfPayment()

        #　収入のフォームのインスタンスを作成
        incomeForm = incomeFormAdd( request.POST, instance = model)
        #　固定費のフォームのインスタンス
        fixedCostForm = fixedCostFormAdd( request.POST, instance = model )
        # 特別費のフォームのインスタンス
        SpFixedCostForm = SpFixedCostFormsAdd( request.POST, instance = model )

        dict = {
            'formOfIncome' : incomeForm,
            'formOfFixedCost' : fixedCostForm,
            'formOfSpFixedCost' : SpFixedCostForm,
        }

        return render(request,'zacklymain/edit.html', dict)

    #フォーム入力の保存
    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            incomeForm = incomeFormAdd( request.POST)
            fixedCostForm = fixedCostFormAdd( request.POST )
            SpFixedCostForm = SpFixedCostFormsAdd( request.POST )

            #３つのフォームのバリデーションが全てOKなら保存
            if incomeForm.is_valid() and fixedCostForm.is_valid() and SpFixedCostForm.is_valid():
                incomeForm.save()
                fixedCostForm.save()
                SpFixedCostForm.save()

            return redirect('/main')
