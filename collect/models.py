from django.db import models
from django.contrib.auth.models import User, AbstractUser


# 个金业务信息收集
class PersonalFinance(models.Model):
    pfid = models.AutoField(primary_key=True, unique=True)
    memo = models.CharField(default='', max_length=300)
    submitter = models.IntegerField()
    bank_subbrch = models.IntegerField()
    submit_time = models.DateTimeField(auto_now_add=True)

    large_deposit = models.CharField(default='0', max_length=100)
    precious_metal = models.CharField(default='0', max_length=100)
    found = models.CharField(default='0', max_length=100)


# 自定义用户模型
class BankUser(AbstractUser):
    # AutoField()
    dept_id = models.IntegerField(null=False, default=0)
    phone = models.CharField(max_length=30, default='')
    lastop_time = models.DateTimeField(auto_now_add=True)
    change_times = models.IntegerField(default=0)

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['email', 'dept_id']

    def __str__(self):
        return self.username + '__' + str(self.dept_id) + \
               '__' + self.phone


# 部门
# 济南分行 <- 历下区支行 <- 历山路支行网点
class Dept(models.Model):
    dept_id = models.IntegerField(primary_key=True, unique=True)
    dept_name = models.CharField(max_length=200, default='')
    parent = models.IntegerField(default=0)
