from django.db import models

from application.dish.models import Dish

name_choice = (
    ('学一食堂', '学一食堂'),
    ('学二食堂', '学二食堂'),
    ('学三食堂', '学三食堂'),
    ('学四食堂', '学四食堂'),
    ('学五食堂', '学五食堂'),
    ('学六食堂', '学六食堂'),
    ('教工食堂', '教工食堂'),
    ('清真食堂', '清真食堂'),
    ('合一厅', '合一厅'),
    ('东区第一食堂', '东区第一食堂'),
    ('鼓瑟轩', '鼓瑟轩'),
    ('西区清真食堂', '西区清真食堂'),
    ('西区第一食堂', '西区第一食堂'),
    ('西区第二食堂', '西区第二食堂'),
    ('西区第三食堂', '西区第三食堂'),
    ('美食苑', '美食苑'),
    ('其他', '其他')
)


class Restaurant(models.Model):
    name = models.CharField(choices=name_choice, default=0, verbose_name="用餐地点", max_length=20  )
    description = models.CharField(max_length=500, default="这里可以吃饭")
    address = models.CharField(max_length=200, null=True, blank=True, default="吃饭就在这里")
    image = models.CharField(max_length=500, default="")

    dishes = models.ManyToManyField(Dish, related_name="restaurant_dishes",
                                    blank=True, default=None)

    def __str__(self):
        return dict(name_choice).get(self.name, "未知")

    class Meta:
        db_table = 'restaurant'
        verbose_name = '餐厅'
        verbose_name_plural = '餐厅s'
