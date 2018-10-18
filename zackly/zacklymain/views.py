from django.shortcuts import render, redirect, get_object_or_404 # テンプレートのレンダリングで使う
from django.http import HttpResponse
from django.template import loader
from datetime import datetime #日時の表示
from django.views import View # 基本汎用クラスビューで使う
# 定義したモデル
from zacklymain.models import balanceOfPayment
#定義したフォーム
from zacklymain.forms import incomeFormAdd, fixedCostFormAdd, SpFixedCostFormsAdd
from django.db.models import Avg, Sum


class top(View):
    """トップページ"""
    def get(self, request, *args, **kwargs ):
        """トップページのGET処理"""
        #ログインした年月を取得。最初だけは当月を表示するので
        nowMonth=datetime.now().month
        modelInstance = get_object_or_404(balanceOfPayment, month=nowMonth )

        dict ={
            'id':modelInstance.month,
            'modelInstance':modelInstance,
            'hour':datetime.now(),
        }

        return render(request,'zacklymain/toppage.html', dict)



class main(View):
    """メインページ"""
    def get(self, request,  *args, **kwargs ):
        """メインページのGET処理。TOP⇒Mainの移動時"""

        id= self.kwargs.get('id')
        modelInstance =get_object_or_404(balanceOfPayment, month=id)

        # それぞれの合計を出す。長いのでこんな書き方になってる。
        # 収入の合計
        sx1 = Sum('amountOfIncome1') + Sum('amountOfIncome2') + Sum('amountOfIncome3') + Sum('amountOfIncome4')
        # 固定費の合計
        sx2 = Sum('amountOfFixedCost1') + Sum('amountOfFixedCost2') + Sum('amountOfFixedCost3') + Sum('amountOfFixedCost4')
        # 特別枠の合計
        sx3 = Sum('amountOfSpFixedCost1') + Sum('amountOfSpFixedCost2') + Sum('amountOfSpFixedCost3') + Sum('amountOfSpFixedCost4')
        amountOfIncome = balanceOfPayment.objects.filter(month=id).aggregate(sx = sx1 - sx2 - sx3 )
        sumOfAmount = balanceOfPayment.objects.filter(month=id).aggregate(sx = sx1 )
        sumOfFixed = balanceOfPayment.objects.filter(month=id).aggregate(sx = sx2 )
        sumOfSpFixed = balanceOfPayment.objects.filter(month=id).aggregate(sx = sx3 ) 
        
        dict={
            'id':id,
            'modelInstance':modelInstance,
            'income': amountOfIncome,
            'soa': sumOfAmount,
            'sof': sumOfFixed,
            'sosf': sumOfSpFixed,
        }
        return render(request,'zacklymain/main.html', dict)

class previous(View):
    """メインページの前月表示"""
    def get(self, request, *args, **kwargs):
        """前月分を表示する"""
        #　一旦計算してから月だけ抜き出す
        #id= self.kwargs.get('id')-1
        #modelInstance=get_object_or_404(balanceOfPayment, month=id)

        # データがないページを指定したら、する前のページで止まる（再表示する）ようにしたい
        try:
            id=self.kwargs.get('id')-1
            modelInstance=balanceOfPayment.objects.get(month=id)

        except balanceOfPayment.DoesNotExist:
            id=self.kwargs.get('id')
            modelInstance=get_object_or_404(balanceOfPayment, month=id)

            # 選んだ月のそれぞれの合計を出す。長いのでこんな書き方になってる。
            # 収入の合計
            sx1 = Sum('amountOfIncome1') + Sum('amountOfIncome2') + Sum('amountOfIncome3') + Sum('amountOfIncome4')
            # 固定費の合計
            sx2 = Sum('amountOfFixedCost1') + Sum('amountOfFixedCost2') + Sum('amountOfFixedCost3') + Sum('amountOfFixedCost4')
            # 特別枠の合計
            sx3 = Sum('amountOfSpFixedCost1') + Sum('amountOfSpFixedCost2') + Sum('amountOfSpFixedCost3') + Sum('amountOfSpFixedCost4')
            amountOfIncome=balanceOfPayment.objects.filter(month=id).aggregate(sx = sx1 - sx2 - sx3 )
            sumOfAmount=balanceOfPayment.objects.filter(month=id).aggregate(sx = sx1 )
            sumOfFixed=balanceOfPayment.objects.filter(month=id).aggregate(sx = sx2 )
            sumOfSpFixed=balanceOfPayment.objects.filter(month=id).aggregate(sx = sx3 )

            dict={
                'id':id,
                'modelInstance':modelInstance,
                'income': amountOfIncome,
                'soa': sumOfAmount,
                'sof': sumOfFixed,
                'sosf': sumOfSpFixed,
            }

            return render(request,'zacklymain/main.html',dict)

        else:
            
            # 選んだ月のそれぞれの合計を出す。長いのでこんな書き方になってる。
            # 収入の合計
            sx1 = Sum('amountOfIncome1') + Sum('amountOfIncome2') + Sum('amountOfIncome3') + Sum('amountOfIncome4')
            # 固定費の合計
            sx2 = Sum('amountOfFixedCost1') + Sum('amountOfFixedCost2') + Sum('amountOfFixedCost3') + Sum('amountOfFixedCost4')
            # 特別枠の合計
            sx3 = Sum('amountOfSpFixedCost1') + Sum('amountOfSpFixedCost2') + Sum('amountOfSpFixedCost3') + Sum('amountOfSpFixedCost4')
            amountOfIncome = balanceOfPayment.objects.filter(month=id).aggregate(sx = sx1 - sx2 - sx3 )
            sumOfAmount = balanceOfPayment.objects.filter(month=id).aggregate(sx = sx1 )
            sumOfFixed = balanceOfPayment.objects.filter(month=id).aggregate(sx = sx2 )
            sumOfSpFixed = balanceOfPayment.objects.filter(month=id).aggregate(sx = sx3 ) 
        
            dict={
                'id':id,
                'modelInstance':modelInstance,
                #'month':month,
                'income': amountOfIncome,
                'soa': sumOfAmount,
                'sof': sumOfFixed,
                'sosf': sumOfSpFixed,
            }
            return render(request,'zacklymain/main.html', dict)


class forward(View):
    """メインページの次月表示"""
    def get(self, request,  *args, **kwargs ):
        """次月分を表示する"""
        #　idを取得
        #id= self.kwargs.get('id')+1
        #modelInstance = get_object_or_404(balanceOfPayment, month=id)

        # データがないページを指定したら、する前のページで止まる（再表示する）ようにしたい
        try:
            id= self.kwargs.get('id')+1
            modelInstance=balanceOfPayment.objects.get(month=id)
        except balanceOfPayment.DoesNotExist:
            id= self.kwargs.get('id')
            modelInstance=get_object_or_404(balanceOfPayment, month=id)

            # 選んだ月のそれぞれの合計を出す。長いのでこんな書き方になってる。
            # 収入の合計
            sx1 = Sum('amountOfIncome1') + Sum('amountOfIncome2') + Sum('amountOfIncome3') + Sum('amountOfIncome4')
            # 固定費の合計
            sx2 = Sum('amountOfFixedCost1') + Sum('amountOfFixedCost2') + Sum('amountOfFixedCost3') + Sum('amountOfFixedCost4')
            # 特別枠の合計
            sx3 = Sum('amountOfSpFixedCost1') + Sum('amountOfSpFixedCost2') + Sum('amountOfSpFixedCost3') + Sum('amountOfSpFixedCost4')
            amountOfIncome=balanceOfPayment.objects.filter(month=id).aggregate(sx = sx1 - sx2 - sx3 )
            sumOfAmount=balanceOfPayment.objects.filter(month=id).aggregate(sx = sx1 )
            sumOfFixed=balanceOfPayment.objects.filter(month=id).aggregate(sx = sx2 )
            sumOfSpFixed=balanceOfPayment.objects.filter(month=id).aggregate(sx = sx3 )

            dict={
                'id':id,
                'modelInstance':modelInstance,
                'income': amountOfIncome,
                'soa': sumOfAmount,
                'sof': sumOfFixed,
                'sosf': sumOfSpFixed,
            }

            return render(request,'zacklymain/main.html',dict)
        
        else:

            # 選んだ月のそれぞれの合計を出す。長いのでこんな書き方になってる。
            # 収入の合計
            sx1 = Sum('amountOfIncome1') + Sum('amountOfIncome2') + Sum('amountOfIncome3') + Sum('amountOfIncome4')
            # 固定費の合計
            sx2 = Sum('amountOfFixedCost1') + Sum('amountOfFixedCost2') + Sum('amountOfFixedCost3') + Sum('amountOfFixedCost4')
            # 特別枠の合計
            sx3 = Sum('amountOfSpFixedCost1') + Sum('amountOfSpFixedCost2') + Sum('amountOfSpFixedCost3') + Sum('amountOfSpFixedCost4')
            amountOfIncome=balanceOfPayment.objects.filter(month=id).aggregate(sx = sx1 - sx2 - sx3 )
            sumOfAmount=balanceOfPayment.objects.filter(month=id).aggregate(sx = sx1 )
            sumOfFixed=balanceOfPayment.objects.filter(month=id).aggregate(sx = sx2 )
            sumOfSpFixed=balanceOfPayment.objects.filter(month=id).aggregate(sx = sx3 )

            dict={
                'id':id,
                'modelInstance':modelInstance,
                'income': amountOfIncome,
                'soa': sumOfAmount,
                'sof': sumOfFixed,
                'sosf': sumOfSpFixed,
            }
            return render(request,'zacklymain/main.html', dict)


class history(View):
    """履歴ページ(必要かはわからない)"""
    def get(self, request, *args, **kwargs):
        """履歴ページのGET"""
        modelInstance = get_object_or_404(balanceOfPayment, month=datetime.now().month)

        income = modelInstance.objects.values('incomeName1','amountOfIncome1') 
        fixedCost = modelInstance.objects.values('fixedCostName1','amountOfFixedCost1')
        d = {
            'id':modelInstance.month,
            'modelInstance':modelInstance,
            'income': income,
            'fixedCost' : fixedCost,
        }


        return render(request,'zacklymain/history.html', d)

    def post(self, request, *args, **kwargs):
        """履歴ページのPOST（いる？）"""

        modelInstance = get_object_or_404(balanceOfPayment, month=datetime.now().month)
        income = modelInstance.objects.values('incomeName1','amountOfIncome1')
        d = {
            'modelInstance':modelInstance,
            'id':modelInstance.month,
            'income': income,
        }
        return render(request,'zacklymain/history.html', d)

#　入力ページ
class edit(View):
    """金額入力ページ"""
    
    def get(self, request, *args, **kwargs):
        """金額入力ページのGET"""
        # idを取得する
        id= self.kwargs.get('id')
        # balanceOfPaymentのModelを作成する
        modelInstance = get_object_or_404(balanceOfPayment, month=id )

        #　収入,固定費,特別費のフォームのインスタンスを作成
        incomeForm = incomeFormAdd( request.POST, instance = modelInstance)
        fixedCostForm = fixedCostFormAdd( request.POST, instance = modelInstance )
        SpFixedCostForm = SpFixedCostFormsAdd( request.POST, instance = modelInstance )

        dict = {
            'id':modelInstance.month,
            'modelInstance':modelInstance,
            'formOfIncome' : incomeFormAdd(instance=modelInstance),
            'formOfFixedCost' : fixedCostFormAdd(instance=modelInstance),
            'formOfSpFixedCost' : SpFixedCostFormsAdd(instance=modelInstance),
        }

        return render(request,'zacklymain/edit.html', dict)

    #フォーム入力の保存
    def post(self, request, *args, **kwargs):
        #データのIDで取得するよー
        id= self.kwargs.get('id')
        modelInstance = get_object_or_404(balanceOfPayment, month=id)

        incomeForm = incomeFormAdd( request.POST, instance=modelInstance)
        fixedCostForm = fixedCostFormAdd( request.POST, instance=modelInstance)
        SpFixedCostForm = SpFixedCostFormsAdd( request.POST, instance=modelInstance)

        #３つのフォームのバリデーションが全てOKなら保存
        if incomeForm.is_valid() and fixedCostForm.is_valid() and SpFixedCostForm.is_valid():
            incomeForm = incomeForm.save(commit=False)
            fixedCostForm = fixedCostForm.save(commit=False)
            SpFixedCostForm = SpFixedCostForm.save(commit=False)
            incomeForm.save()
            fixedCostForm.save()
            SpFixedCostForm.save()
            #リダイレクトは'app_name:pathname'で指定しないと
            return redirect('zacklymain:main', id=id)

        dict={
            'id':modelInstance.month,
            'modelInstance': modelInstance,
            'formOfIncome' : incomeFormAdd(instance=modelInstance),
            'formOfFixedCost' : fixedCostFormAdd(instance=modelInstance),
            'formOfSpFixedCost' : SpFixedCostFormsAdd(instance=modelInstance),
        }
        return render(request,'zacklymain:main', dict)
