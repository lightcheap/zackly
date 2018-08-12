# Generated by Django 2.0.7 on 2018-08-12 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zacklymain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FixedCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=30, verbose_name='品目')),
                ('amountOfFixedCost', models.IntegerField(default=0, verbose_name='固定')),
            ],
        ),
    ]
