# 存储了用户的基本信息

from django.contrib.auth.models import AbstractUser
from django.db import models

from application.comment.models import Comment
from application.dish.models import Dish
from application.restaurant.models import Restaurant

default_avatar = "https://pigkiller-011955-1319328397.cos.ap-beijing.myqcloud.com/img/202407241830349.avif"


class User(AbstractUser):
    id = models.AutoField(primary_key=True, auto_created=True, verbose_name='用户ID', editable=False)
    email = models.EmailField(unique=True, verbose_name='邮箱',
                              error_messages={'unique': '该邮箱已被注册'}, blank=False)
    password = models.CharField(max_length=256, verbose_name='密码')
    school = models.CharField(max_length=200,verbose_name="学院",blank=True,default="计算机学院")

    gender_choices = (
        ('secret', '不设置/保密'),
        ('male', '男'),
        ('female', '女'),
    )
    gender = models.CharField(choices=gender_choices, max_length=32, default='保密', verbose_name='性别')
    motto = models.CharField(max_length=256, default='这个人很懒，什么都没有留下', verbose_name='个性签名')
    avatar = models.CharField(default=default_avatar, verbose_name='头像', max_length=500)

    # 该用户发布过的评论
    comments = models.ManyToManyField(Comment, related_name='user_comments', blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users',  # 这里将 related_name 改为 'custom_users'
        related_query_name='custom_user',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users',  # 这里将 related_name 改为 'custom_users'
        related_query_name='custom_user',
        blank=True,
    )

    # 该用户收藏的评论
    collected_comments = models.ManyToManyField(Comment, related_name='collected_user', blank=True)
    # 该用户收藏的餐馆
    collected_restaurants = models.ManyToManyField(Restaurant, related_name='collected_user', blank=True)
    # 该用户收藏的菜品
    collected_dishes = models.ManyToManyField(Dish, related_name='collected_user', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        ordering = ['-date_joined']
        verbose_name = '用户'
        verbose_name_plural = '用户'
        swappable = "AUTH_USER_MODEL"
