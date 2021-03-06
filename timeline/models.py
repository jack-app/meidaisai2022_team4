from django.conf import settings
from django.db import models
from django.utils import timezone
from account.models import Account

# 年
class Year(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    span = models.IntegerField(default=12)
    start_date = models.DateField()
    published_date = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.name

# 月
class Month(models.Model):
    year_id = models.ForeignKey(Year, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    span = models.IntegerField(default=4)
    start_date = models.DateField()
    published_date = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.name

# 週
class Week(models.Model):
    month_id = models.ForeignKey(Month, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    span = models.IntegerField(default=7)
    start_date = models.DateField()
    published_date = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.name

# イベント
class Event(models.Model):
    #week_id = models.ForeignKey(Week, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    detail = models.TextField()
    date = models.DateField(default=timezone.now)
    published_date = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.name