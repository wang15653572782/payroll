# Generated by Django 4.2.4 on 2023-09-08 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_name', models.CharField(max_length=255, verbose_name='员工姓名')),
                ('worker_type', models.SmallIntegerField(choices=[(0, '小时工'), (1, '受薪工'), (2, '委托工')], verbose_name='雇员类型')),
                ('worker_address', models.TextField(max_length=1024, verbose_name='邮寄地址')),
                ('SocialSecurityNumber', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='社会保险号')),
                ('TaxCut', models.IntegerField(default=0, verbose_name='标准减税')),
                ('OtherCost', models.IntegerField(choices=[(0, '401k'), (1, '医疗')], default=0, verbose_name='其他扣除')),
                ('Tel', models.CharField(max_length=20, verbose_name='电话号码')),
                ('Wages', models.IntegerField(default=0, verbose_name='薪金')),
                ('CommissionRate', models.FloatField(default=0, verbose_name='佣金率')),
                ('HourLimit', models.IntegerField(default=0, max_length=20, verbose_name='小时限制')),
            ],
        ),
    ]
