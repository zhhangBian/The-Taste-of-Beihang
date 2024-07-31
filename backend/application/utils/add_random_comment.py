import os
import re

import django

# 设置环境变量并初始化 Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WhatToEatInHang.settings')
django.setup()

from application.users.models import User
from application.comment.models import Comment
from application.dish.models import Dish
import random


def generate_random_real_float(a, b):
    return round(random.uniform(a, b), 1)


def generate_random_float(a, b):
    # 可能的整数部分列表
    integers = list(range(a, b))
    # 随机选择一个整数，并构造对应的浮点数（整数+0.5，除了18直接返回）
    chosen_int = random.choice(integers)
    havePointFive = random.choice([True, False])
    if havePointFive:
        return float(f"{chosen_int}.0")
    else:
        return float(f"{chosen_int}.5")


def clean_string(text):
    # 正则表达式匹配所有非中文和非英文字符
    pattern = r'[^\u4e00-\u9fffA-Za-z]'
    # 使用re.sub()替换所有匹配的字符为空字符串
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text


heads = ["天哪！", "震惊！", "快来这个宝藏食堂"]
comments = ["哈哈哈好好吃", "好吃到跺脚", "不愧是北航水平", '香甜软糯啊']

for i in range(100):
    dish = Dish.objects.order_by('?').first()
    author = User.objects.order_by('?').first()
    print(dish.name)

    comment, created = Comment.objects.update_or_create(
        title=clean_string(str(dish.name) + "热评"),
        content=random.choice(heads) + random.choice(comments),
        image=dish.image,

        grade=generate_random_real_float(4, 5),
        price=generate_random_real_float(4, 5),
        flavour=generate_random_float(0, 2),
        waiting_time=random.randint(1, 100),

        restaurant_name=dish.restaurant_name,
        dish_name=dish.name,
        author_id=author.id
    )
