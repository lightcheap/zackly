# Generated by Django 2.0.7 on 2018-09-17 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zacklymain', '0007_auto_20180918_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='spfixedcost',
            name='amountOfSpFixedCost2',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='特別'),
        ),
        migrations.AddField(
            model_name='spfixedcost',
            name='amountOfSpFixedCost3',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='特別'),
        ),
        migrations.AddField(
            model_name='spfixedcost',
            name='amountOfSpFixedCost4',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='特別'),
        ),
        migrations.AddField(
            model_name='spfixedcost',
            name='item2',
            field=models.CharField(blank=True, default=' ', max_length=30, null=True, verbose_name='品目'),
        ),
        migrations.AddField(
            model_name='spfixedcost',
            name='item3',
            field=models.CharField(blank=True, default=' ', max_length=30, null=True, verbose_name='品目'),
        ),
        migrations.AddField(
            model_name='spfixedcost',
            name='item4',
            field=models.CharField(blank=True, default=' ', max_length=30, null=True, verbose_name='品目'),
        ),
    ]
