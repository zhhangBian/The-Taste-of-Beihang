# 对于菜品的评论
# 由用户和菜共享

from django.db import models

default_img = "https://pigkiller-011955-1319328397.cos.ap-beijing.myqcloud.com/img/202407241935479.jpg"


class Comment(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    image = models.CharField(default=default_img, verbose_name='图片')

    grade = models.IntegerField(default=0,
                                choices=(
                                    (0, '未评分'), (1, '一星'),
                                    (2, '二星'), (3, '三星'),
                                    (4, '四星'), (5, '五星')
                                ))
    avg_price = models.IntegerField(default=0)

    # 可能无法定位到具体的菜品
    # dish = models.ForeignKey('dish.Dish', on_delete=models.CASCADE, related_name="comments")

    # 发布者
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="comments")
    # 发布的地点
    restaurant = models.ForeignKey('restaurant.Restaurant', on_delete=models.CASCADE, related_name="comments")

    agree_count = models.IntegerField(default=0)
    agree_authors = models.ManyToManyField('users.User', related_name='agree_comments')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
