from django.db import models

from application.dish.models import Dish

name_choice = (
    (1, '学一'),
    (2, '学二'),
    (3, '学三'),
    (4, '学四'),
    (5, '学五'),
    (6, '学六'),
    (20, '美食苑'),
    (114514, '其他')
)


class Restaurant(models.Model):
    name = models.IntegerField(choices=name_choice, default=0, verbose_name="用餐地点")
    description = models.CharField(max_length=500, default="这里可以吃饭")
    address = models.CharField(max_length=200, null=True, blank=True, default="吃饭就在这里")
    image = models.CharField(max_length=500, default="")

    dishes = models.ForeignKey(Dish, on_delete=models.CASCADE,
                               related_name="restaurant_dishes",
                               null=True, blank=True, default=None)

    def __str__(self):
        return dict(name_choice).get(self.name, "未知")

    class Meta:
        db_table = 'restaurant'
        verbose_name = '餐厅'
        verbose_name_plural = '餐厅s'
