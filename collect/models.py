from django.db import models
from django.contrib.auth.models import User, AbstractUser


# 个金业务信息收集
class PersonalFinance(models.Model):
    pfid = models.AutoField(primary_key=True, unique=True)
    memo = models.CharField(default='')
    submitter = models.IntegerField(null=False)
    bank_subbrch = models.IntegerField()
    submit_time = models.DateTimeField(auto_now_add=True)

    large_deposit = models.CharField(default='0')
    precious_metal = models.CharField(default='0')
    found = models.CharField(default='0')


# 自定义用户模型
class BankUser(AbstractUser):
    dept_id = models.IntegerField(null=False)
    phone = models.CharField(max_length=30, default='')
    lastop_time = models.DateTimeField(auto_now_add=True)
    change_times = models.IntegerField(default=0)

    def __str__(self):
        return self.username + '__' + self.dept_id + \
               '__' + self.phone


# 部门
# 济南分行 <- 历下区支行 <- 趵突泉网点
class Dept(models.Model):
    dept_id = models.IntegerField(primary_key=True, unique=True, null=False)
    dept_name = models.CharField(max_length=200, default='')
    parent = models.IntegerField(default=0)
