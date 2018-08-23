from django.shortcuts import render, redirect # テンプレートのレンダリングで使う
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.views import View # 基本汎用クラスビューで使う
# from .forms import incomeFormAdd # 定義したフォーム
from .models import Income # 定義したモデル

from .forms import NameForm, incomeFormAdd #チュートリアルで追加した分


class top(View):
    def get(self, request, *args, **kwargs):
        d ={
            'hour':datetime.now(),
        }    
        #template = loader.get_template('zacklymain/toppage.html')
        return render(request,'zacklymain/toppage.html', d)


def get_name(request):
    #　POSTリクエストの場合、フォームデータを処理
    if request.method =='POST':
        #フォームインスタンスを作成し、リクエストからのデータを入力
        form = NameForm(request.POST)
        # バリデーションの確認
        if form.is_valid():
            #必要に応じて form.cleaned_dataでデータを処理する。
            #新しいURLにリダイレクトする
            return redirect('/thanks/')

        #もしGETかその他の方法で空白のフォームを作成するとき
        else:
            form = NameForm()
        return render( request, 'toppage.html',{'form' :form } )


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

    def post(self, request, *args, **kwargs):
        income = Income.objects.values('item','amountOfIncome')
        d = {
            'income': income,
        }
        return render(request,'zacklymain/history.html', d)

class edit(View):
    def get(self, request, *args, **kwargs):
        # IncomeのModelを作成する
        member = Income()

        form = incomeFormAdd( request.POST, instance = member)


        return render(request,'zacklymain/edit.html', dict(form=form))
        
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
            return redirect('history/')

    else:
        form = incomeFormAdd( request.POST, instance = member)

    
    return render(request,'edit/', dict(form=form) )
