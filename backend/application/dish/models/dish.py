# 描述了具体的菜品

from django.db import models

default_img = "https://pigkiller-011955-1319328397.cos.ap-beijing.myqcloud.com/img/202407241935479.jpg"


class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name='菜品名称')
    image = models.CharField(default=default_img, verbose_name='图片', max_length=500)
    address = models.CharField(max_length=100, verbose_name='餐厅地址')

    price = models.FloatField(verbose_name='价格')
    description = models.TextField(max_length=500, verbose_name='描述')
    overall_rating = models.FloatField(verbose_name='总体评分')
    flavor_rating = models.FloatField(verbose_name='风味评分')
    waiting_time = models.FloatField(verbose_name='等待时间')

    # dish唯一对应一个餐厅
    restaurant = models.ForeignKey('restaurant.Restaurant', on_delete=models.CASCADE, verbose_name='餐厅')

    # 一个菜品可以有多个评论
    comments = models.ManyToManyField('comment.Comment', related_name='dish_comments', verbose_name='评论')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'dish'
        ordering = ['-name']
        verbose_name = '菜品'
        verbose_name_plural = '菜品'
