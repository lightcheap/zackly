from django.contrib import admin
from .models import balanceOfPayment


# class BOPModelAdmin(admin.ModelAdmin):
    #一覧表示のフィールドを変更
#    listDisplay = ('year', 'month',)


# Register your models here.
admin.site.register(balanceOfPayment)