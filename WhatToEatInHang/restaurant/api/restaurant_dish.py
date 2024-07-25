import random
import re

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest
from django.utils import timezone
from django.views.decorators.http import require_POST, require_GET, require_http_methods

from restaurant.models import Restaurant
from users.models import User
from comment.models import Comment
from utils.data_process import parse_data
from utils.response import *

places = ["学一", "学二", "学三", "学四", "学五", "学六", "美食苑", "其他"]
dishes = ["麻辣香锅", "猪脚饭", "兰州拉面", "黄焖鸡米饭", "汉堡", "", "淄博烧烤", "铁板烧", "茶香鸡"]


# 获取评论的集合
def serialize_comments(comments) -> list:
    comments_list = []

    for comment in comments:
        comment_dict = {
            'id': comment.id,
            'title': comment.title,
            'content': comment.content,
            'date': comment.date.strftime('%Y-%m-%d %H:%M:%S'),  # 格式化日期
            'image': comment.image,
            'grade': comment.grade,
            'avg_price': comment.avg_price,
            'author': comment.author.username,  # 假设我们只想要用户名
            'restaurant': comment.restaurant.name,  # 假设 Restaurant 模型有一个 name 字段
            'agree_count': comment.agree_count,
        }
        comments_list.append(comment_dict)

    return comments_list


def matches_search(comment, search_string):
    # 将搜索字符串转换为正则表达式模式
    # 这里使用了 re.escape 来确保搜索字符串中的任何特殊字符都被正确处理
    escaped_search_string = re.escape(search_string)
    pattern = f"{escaped_search_string}(?={escaped_search_string})"

    # 使用正则表达式搜索评论标题
    return bool(re.search(pattern, comment.title, re.IGNORECASE))


@response_wrapper
@require_GET
def get_recommendation(request):
    place = random.choice(places)
    dish = random.choice(dishes)

    return success_response({
        "recommendation": str("在" + place + "吃" + dish),
        "place": place,
        "dish": dish,
    })


@response_wrapper
@require_POST
def search_comment(request):
    post_data = parse_data(request)
    search = post_data.get('search')

    comments_fit = list(filter(lambda comment: matches_search(comment, search),
                               Comment.objects.all()))
    comments_fit_serialized = serialize_comments(comments_fit)

    return success_response({
        "comments": comments_fit_serialized,
        "size": len(comments_fit_serialized)
    })


@response_wrapper
@require_POST
def search_comment_restaurant(request: HttpRequest):
    post_data = parse_data(request)
    search = post_data.get('search')
    restaurant_name = post_data.get('restaurant_name')
    restaurant = Restaurant.objects.get(name=restaurant_name)

    comments_fit = list(filter(lambda comment: matches_search(comment, search),
                               restaurant.comments.objects.all()))
    comments_fit_serialized = serialize_comments(comments_fit)

    return success_response({
        "comments": comments_fit_serialized,
        "size": len(comments_fit_serialized)
    })
