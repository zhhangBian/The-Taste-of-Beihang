# 记录了用餐信息

from django.db import models


class Record(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, verbose_name='用餐记录ID', editable=False)
    date = models.DateTimeField(auto_now_add=True, verbose_name='日期')
    dish_name = models.CharField(max_length=200, verbose_name="餐品名称", blank=False)
    price = models.FloatField(default=0, verbose_name="价格")

    def __str__(self):
        return "用餐记录" + str(id)

    class Meta:
        db_table = 'record'
        verbose_name = '用餐记录'
        verbose_name_plural = '用餐记录'
        ordering = ['-date']
