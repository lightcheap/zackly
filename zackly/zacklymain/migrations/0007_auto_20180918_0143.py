# Generated by Django 2.0.7 on 2018-09-17 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zacklymain', '0006_auto_20180918_0108'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixedcost',
            name='amountOfFixedCost2',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='固定'),
        ),
        migrations.AddField(
            model_name='fixedcost',
            name='amountOfFixedCost3',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='固定'),
        ),
        migrations.AddField(
            model_name='fixedcost',
            name='amountOfFixedCost4',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='固定'),
        ),
        migrations.AddField(
            model_name='fixedcost',
            name='amountOfFixedCost5',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='固定'),
        ),
        migrations.AddField(
            model_name='fixedcost',
            name='item2',
            field=models.CharField(blank=True, default=' ', max_length=30, null=True, verbose_name='品目'),
        ),
        migrations.AddField(
            model_name='fixedcost',
            name='item3',
            field=models.CharField(blank=True, default=' ', max_length=30, null=True, verbose_name='品目'),
        ),
        migrations.AddField(
            model_name='fixedcost',
            name='item4',
            field=models.CharField(blank=True, default=' ', max_length=30, null=True, verbose_name='品目'),
        ),
        migrations.AddField(
            model_name='fixedcost',
            name='item5',
            field=models.CharField(blank=True, default=' ', max_length=30, null=True, verbose_name='品目'),
        ),
    ]
