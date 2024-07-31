import csv
import os

import django

# 设置环境变量并初始化 Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WhatToEatInHang.settings')
django.setup()

from application.comment.models import Comment
from application.dish.models import Dish
from application.users.models import User
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


with open("data/comment_data.csv", "r", encoding='utf-8') as data_file:
    data = csv.DictReader(data_file)

    for row in data:
        author = User.objects.order_by('?').first()

        dish_name = row['dish_name']
        image = row['image']
        restaurant_name = row['restaurant_name']
        address = row['address']
        content = row['content']

        title = row['title']

        try:
            dish = Dish.objects.get(name=dish_name)
        except Dish.DoesNotExist:
            dish, created = Dish.objects.update_or_create(
                name=dish_name,
                image=image,
                address=address,
                restaurant_name=restaurant_name,
                description=content,
            )
            print("create dish of " + str(dish_name) + " in " + str(restaurant_name))

        comment, created = Comment.objects.update_or_create(
            title=title,
            content=content,
            image=image,

            grade=generate_random_real_float(4, 5),
            price=generate_random_real_float(4, 5),
            flavour=generate_random_float(0, 2),
            waiting_time=random.randint(1, 100),

            restaurant_name=restaurant_name,
            dish_name=dish_name,
            author_id=author.id
        )
        print("create comment " + str(title) + " of " + str(dish_name))
