"""
这是储存用户基本信息的模型
"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class Comment(AbstractUser):
    id = models.AutoField(primary_key=True, auto_created=True, verbose_name='评论ID', editable=False)
    content = models.TextField(verbose_name='评论内容')
    img = models.ImageField(upload_to='avatar/', default='avatar/default.png', verbose_name='头像')
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='评论用户')
    restaurant = models.ForeignKey('restaurant.Restaurant', on_delete=models.CASCADE, verbose_name='评论餐厅')

    

    subscriptions = models.ManyToManyField('self', symmetrical=False, related_name='subscribers', through='Subscribe')
    send_messages = models.ManyToManyField('self', symmetrical=False, related_name='received_by', through='Message')
    collections = models.ManyToManyField('restaurant.Restaurant', related_name='collectors', through='Collection')

    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-date_joined']
        verbose_name = '用户'
        verbose_name_plural = '用户'
