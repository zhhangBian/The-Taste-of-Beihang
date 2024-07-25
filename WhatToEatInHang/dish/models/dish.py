# 描述了具体的菜品

from django.db import models

from comment.models import Comment
from restaurant.models import Restaurant

default_img = "https://pigkiller-011955-1319328397.cos.ap-beijing.myqcloud.com/img/202407241935479.jpg"


class Dish(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(default=default_img, verbose_name='图片')
    address = models.CharField(max_length=100)

    price = models.FloatField()
    description = models.TextField(max_length=500)
    overall_rating = models.FloatField()
    flavor_rating = models.FloatField()
    waiting_time = models.FloatField()

    # dish唯一对应一个餐厅
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant')
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
