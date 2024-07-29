# 描述了具体的菜品

from django.db import models

default_img = "https://pigkiller-011955-1319328397.cos.ap-beijing.myqcloud.com/img/202407241935479.jpg"


class Dish(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, verbose_name='评论ID', editable=False)
    name = models.CharField(max_length=100, verbose_name='菜品名称', default="菜品名称")
    image = models.CharField(default=default_img, verbose_name='图片', max_length=500)

    address = models.CharField(default="默认地址", max_length=100, verbose_name='餐厅地址')
    restaurant_name = models.CharField(default="默认餐厅", verbose_name='菜品餐厅', max_length=500)

    description = models.TextField(max_length=500, verbose_name='描述', default="暂时还没有描述。/")

    price = models.FloatField(verbose_name='价格', default=0)
    overall_rating = models.FloatField(verbose_name='总体评分', default=0)
    flavor_rating = models.FloatField(verbose_name='风味评分', default=0)
    waiting_time = models.FloatField(verbose_name='等待时间', default=0)

    # 一个菜品可以有多个评论
    comments = models.ManyToManyField('comment.Comment', related_name='dish_comments', verbose_name='评论', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'dish'
        ordering = ['-name']
        verbose_name = '菜品'
        verbose_name_plural = '菜品'
