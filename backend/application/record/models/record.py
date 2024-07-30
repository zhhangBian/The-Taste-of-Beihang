# 记录了用餐信息

from django.db import models


class Record(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, verbose_name='用餐记录ID', editable=False)
    time = models.CharField(max_length=200, verbose_name='日期', blank=True)
    dish_name = models.CharField(max_length=200, verbose_name="餐品名称", blank=False, default="反正吃了什么")
    restaurant_name = models.CharField(max_length=200, verbose_name="所属食堂", default="默认食堂")
    price = models.FloatField(default=0, verbose_name="价格")

    def __str__(self):
        return "用餐记录" + str(id)

    class Meta:
        db_table = 'record'
        verbose_name = '用餐记录'
        verbose_name_plural = '用餐记录'
