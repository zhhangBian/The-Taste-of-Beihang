from django.views.decorators.http import require_GET

from application.comment.models import Comment
from application.dish.models import Dish
from application.utils.data_process import parse_data
from application.utils.response import *


# 获取评论的集合
def serialize_dish_comments(dish: 'Dish') -> list:
    """
    返回某一道菜的所有评论的信息序列
    """
    comments_list = []
    dish_comments = Comment.objects.filter(dish_name=dish.name)

    for comment in dish_comments:
        comment_dict = {
            'title': comment.title,
            'content': comment.content,
            'date': comment.date,
            'image': comment.image,

            'grade': comment.grade,
            'price': comment.price,
            'flavour': comment.flavour,
            'waiting_time': comment.waiting_time,

            'author_id': comment.author_id,
        }
        comments_list.append(comment_dict)

    return comments_list


@response_wrapper
@require_GET
def get_dish_comments(request):
    user = request.user
    post_data = parse_data(request)

    address = post_data.get("dish_address")
    name = post_data.get("dish_name")

    dish = Dish.objects.get(name=name, address=address)
    comments_count = dish.dish_comments.count()

    return success_response({
        "comments_count": comments_count,
        "comments_list": serialize_dish_comments(dish),
    })
