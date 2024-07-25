from django.http import HttpRequest
from django.views.decorators.http import require_GET

from utils.response import fail_response, ErrorCode, success_response, response_wrapper
from ..models import Dish


# 获取评论的集合
def serialize_comments(dish: 'Dish') -> list:
    comments_list = []
    dish_comments = dish.comments.all()

    for comment in dish_comments:
        comment_dict = {
            'name': comment.name,
            'image': comment.image,
            'address': comment.address,
            'price': comment.price,
            'description': comment.description,
            'overall_rating': comment.overall_rating,
            'flavor_rating': comment.flavor_rating,
            'waiting_time': comment.waiting_time,
        }
        comments_list.append(comment_dict)

    return comments_list


@response_wrapper
@require_GET
def get_dish_comments(request):
    address = request.dish_address
    name = request.dish_name

    dish = Dish.objects.get(name=name, address=address)
    comments_count = dish.comments.count()

    return success_response({
        "comments_count": comments_count,
        "comments_list": serialize_comments(dish),
    })
