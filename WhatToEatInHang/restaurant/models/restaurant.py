from django.db import models

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
    detail_addr = models.CharField(max_length=200, null=True, blank=True, default="吃饭就在这里")
    img = models.ImageField(upload_to='restaurant/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', '-date_joined']
        verbose_name = '餐厅'
        verbose_name_plural = '用户s'
