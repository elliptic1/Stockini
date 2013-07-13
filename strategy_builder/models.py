from django.db import models

# Create your models here.

class strategy(models.Model):
    strategy_id = models.AutoField(max_length=8, primary_key=True)
    stock_symbol = models.CharField(max_length=5)
    event_one = models.IntegerField(max_length=8)
    event_two = models.IntegerField(max_length=8)
    event_three = models.IntegerField(max_length=8)
    action = models.IntegerField(max_length=2)


class action(models.Model):
    action_id = models.AutoField(max_length=1, primary_key=True)
    ACTIONS = (
        (u'buy', u'Buy'),
        (u'short_buy', u'Short Buy'),
        (u'sell', u'Sell'),
        (u'short_sell', u'Short Sell'),
        (u'hold', u'Hold'),
    )
    action = models.CharField(max_length=10, choices=ACTIONS) # buy or sell


class event(models.Model):
    event_id = models.AutoField(max_length=8, primary_key=True)
    cross_line = models.CharField(max_length=20) # e.g. Bollinger Band or SMA
    cross_direction = models.IntegerField(max_length=1) # 1 = up, 2 = down
    cross_slope = models.IntegerField(max_length=3)
