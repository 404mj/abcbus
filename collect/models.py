from django.db import models


class PersonalFinance(models.Model):
    pfid = models.AutoField(primary_key=True)
    memo = models.CharField(default='')
    subbrch_net = models.IntegerField()
    bank_subbrch = models.IntegerField()
    submitter = models.CharField(max_length=50, default='',)
    submit_time = models.DateTimeField(auto_now_add=True)

    large_deposit = models.CharField(default='0')
    precious_metal = models.CharField(default='0')
    found = models.CharField(default='0')
