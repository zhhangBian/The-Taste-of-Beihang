# 对于菜品的评论
# 由用户和菜共享

from django.db import models

default_img = "https://pigkiller-011955-1319328397.cos.ap-beijing.myqcloud.com/img/202407241935479.jpg"


class Comment(models.Model):
    # id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    image = models.CharField(default=default_img, verbose_name='图片', max_length=500)

    grade = models.IntegerField(default=0,
                                choices=(
                                    (0, '未评分'), (1, '一星'),
                                    (2, '二星'), (3, '三星'),
                                    (4, '四星'), (5, '五星')
                                ))
    price = models.FloatField(default=0)
    flavour = models.FloatField(default=0)
    waiting_time = models.FloatField(default=0)

    author_id = models.IntegerField(default=0)
    dish_name = models.CharField(max_length=100)
    restaurant_name = models.CharField(max_length=200)

    # agree_count = models.IntegerField(default=0)
    # agree_author_ids = models.ManyToManyField(int, related_name='agree_comments')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'comments'
        ordering = ['-date']
