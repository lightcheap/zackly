from django.shortcuts import render, get_object_or_404
# 追加分
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic #ジェネリックビュー用
from django.views import View # 基本汎用クラスビューで使う
from datetime import datetime #日時の表示
from zacklymain.models import balanceOfPayment #モデル

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class ProfileView(View):
    def get(self, request, *args, **kwargs ):
        #当月分を表示する用
        #ここで当月分のデータがないとエラーになるのでないならつくる

        try:#今月分のデータを取得してみる
            nowMonth = datetime.now().month
            modelInstance = balanceOfPayment.objects.get(month=nowMonth)

        except balanceOfPayment.DoesNotExist: #それが404が出るなら今月分のデータを作成する
            modelInstance = balanceOfPayment()
            modelInstance.month = nowMonth
            modelInstance.save()

        dict={
            'id':modelInstance.month,
            'modelInstance':modelInstance,
        }
        return render(request,'accounts/profile.html', dict)