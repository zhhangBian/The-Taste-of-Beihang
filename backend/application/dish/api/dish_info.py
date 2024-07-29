import json

from django.http import HttpRequest
from django.views.decorators.http import require_GET

from application.comment.models import Comment
from application.dish.models import Dish
from application.users.api import User
from application.utils.response import *


@response_wrapper
@require_GET
def get_dish_info(request: HttpRequest):
    body = json.loads(request.body.decode('utf-8'))

    restaurant_name = body.get('restaurant_name', '')
    dish_name = body.get('dish_name', '')

    dishes = Dish.objects.filter(name=dish_name, restaurant_name=restaurant_name)
    if not dishes.exists():
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '菜品不存在')

    dishes_basics = [
        {
            "name": dish.name,
            "image": dish.image,

            "address": dish.address,
            "restaurant_name": dish.restaurant_name,

            "description": dish.description,

            "prices": dish.price,
            "overall_rating": dish.overall_rating,
            "flavor_rating": dish.flavor_rating,
            "waiting_time": dish.waiting_time,
        } for dish in dishes
    ]

    return success_response({
        "dishes_info": dishes_basics,
    })


@response_wrapper
@require_GET
def get_dish_info_id(request: HttpRequest, id: int):
    dish = Dish.objects.filter(id=id).first()

    comments = Comment.objects.filter(dish_name=dish.name)
    comments_list = []
    for comment in comments:
        author = User.objects.get(id=comment.author_id)
        comment_dict = {
            'id': comment.id,
            'title': comment.title,
            'content': comment.content,
            'date': comment.date.strftime('%Y-%m-%d %H:%M:%S'),  # 格式化日期
            'image': comment.image,

            'grade': comment.grade,
            'price': comment.price,
            'flavour': comment.flavour,
            'waiting_time': comment.waiting_time,

            'restaurant_name': comment.restaurant_name,
            'dish_name': comment.dish_name,
            'dish_id': dish.id,
            'author_id': comment.author_id,
            'author_name': author.username,
            'avatar': author.avatar
        }
        comments_list.append(comment_dict)
    print(comments_list)

    return success_response({
        "name": dish.name,
        "image": dish.image,

        "address": dish.address,
        "restaurant_name": dish.restaurant_name,

        "description": dish.description,

        "prices": dish.price,
        "overall_rating": dish.overall_rating,
        "flavor_rating": dish.flavor_rating,
        "waiting_time": dish.waiting_time,

        "comment_num": len(comments_list),
        "comments": comments_list,
    })
