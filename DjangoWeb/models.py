from django.db import models
from django.contrib.auth.models import User
# Create your models here.
worktype=[
    (0,"小时工"),
    (1,"受薪工"),
    (2,"委托工"),
]
othercost=[
    (0,"401k"),
    (1,"医疗"),
]
class Worker(models.Model):
    worker_name = models.CharField(max_length=255,blank=False,verbose_name="员工姓名")
    worker_type = models.SmallIntegerField(choices=worktype,blank=False,verbose_name="雇员类型")
    worker_address = models.TextField(max_length=1024,blank=False,verbose_name="邮寄地址")
    SocialSecurityNumber = models.CharField(default="", max_length=50, blank=True, null=True,verbose_name="社会保险号")
    TaxCut = models.IntegerField(verbose_name="标准减税",default=0)
    OtherCost = models.IntegerField(choices=othercost,blank=False,default=0,verbose_name="其他扣除")
    Tel = models.CharField(max_length=20,blank=False,verbose_name="电话号码")
    if worker_type == 0:
        WagesPerHour = models.IntegerField(verbose_name="小时工资",default=0)
    else:
        Wages = models.IntegerField(verbose_name="薪金",default=0)
    CommissionRate = models.FloatField(verbose_name="佣金率",default=0)
    HourLimit = models.IntegerField(default=0,verbose_name="小时限制")



