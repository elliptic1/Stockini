from django.db import models

# Create your models here.

class stock(models.Model):
    strategy_id = models.AutoField(max_length=8, primary_key=True)
    stock_symbol = models.CharField(max_length=5)
    event_one = models.IntegerField(max_length=8)

