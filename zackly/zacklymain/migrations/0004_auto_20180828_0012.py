# Generated by Django 2.0.7 on 2018-08-27 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zacklymain', '0003_spfixedcost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixedcost',
            name='amountOfFixedCost',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='固定'),
        ),
        migrations.AlterField(
            model_name='fixedcost',
            name='item',
            field=models.CharField(blank=True, default=' ', max_length=30, null=True, verbose_name='品目'),
        ),
        migrations.AlterField(
            model_name='income',
            name='amountOfIncome',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='収入'),
        ),
        migrations.AlterField(
            model_name='income',
            name='item',
            field=models.CharField(blank=True, default=' ', max_length=30, null=True, verbose_name='品目'),
        ),
        migrations.AlterField(
            model_name='spfixedcost',
            name='amountOfSpFixedCost',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='特別'),
        ),
        migrations.AlterField(
            model_name='spfixedcost',
            name='item',
            field=models.CharField(blank=True, default=' ', max_length=30, null=True, verbose_name='品目'),
        ),
    ]
