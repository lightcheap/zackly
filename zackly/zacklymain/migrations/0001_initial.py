# Generated by Django 2.0.7 on 2018-08-12 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=30, verbose_name='品目')),
                ('amountOfIncome', models.IntegerField(default=0, verbose_name='収入')),
            ],
        ),
    ]
