# 代表了用户的收藏接口
import json

from django.contrib.auth import authenticate
from django.http import HttpRequest

from .auth import *
from ...comment.models import Comment
from ...dish.models import Dish
from ...restaurant.models import Restaurant
from ...utils.response import *


# todo 这里应该怎么获取用户？
def get_user_and_obj(request: HttpRequest):
    body = json.loads(request.body.decode('utf-8'))
    username = body.get('username')
    password = body.get('password')
    # 使用Django的authenticate函数验证用户名和密码
    user = authenticate(username=username, password=password)
    ret_type = body['type']
    if ret_type == 'comment':
        comment_id = body['comment_id']
        obj = Comment.objects.get(id=comment_id)
    elif ret_type == 'restaurant':
        restaurant_id = body['restaurant_id']
        obj = Restaurant.objects.get(id=restaurant_id)
    else:
        dish_id = body['dish_id']
        obj = Dish.objects.get(id=dish_id)
    return user, obj


@response_wrapper
@require_GET
def user_collect_comment(request: HttpRequest):
    user, comment = get_user_and_obj(request)
    if comment is None:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '评论不存在')
    else:  # add comment to collected_comments
        user.collected_comments.add(comment)
        return success_response({
            "id": user.id,
            "comment_id": comment.id,
        })


@response_wrapper
@require_GET
def user_collect_restaurant(request: HttpRequest):
    user, restaurant = get_user_and_obj(request)
    if restaurant is None:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '餐馆不存在')
    else:  # add restaurant to collected_restaurants
        user.collected_restaurants.add(restaurant)
        return success_response({
            "id": user.id,
            "restaurant_id": restaurant.id,
        })


@response_wrapper
@require_GET
def user_collect_dish(request: HttpRequest):
    user, dish = get_user_and_obj(request)
    if dish is None:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '菜品不存在')
    else:  # add dish to collected_dishes
        user.collected_dishes.add(dish)
        return success_response({
            "id": user.id,
            "dish_id": dish.id,
        })


def user_delete_comment(request: HttpRequest):
    user, comment = get_user_and_obj(request)
    user.collected_comments.remove(comment)
    return success_response({
        "id": user.id,
        "comment_id": comment.id,
    })


def user_delete_restaurant(request: HttpRequest):
    user, restaurant = get_user_and_obj(request)
    user.collected_restaurants.remove(restaurant)
    return success_response({
        "id": user.id,
        "restaurant_id": restaurant.id,
    })


def user_delete_dish(request: HttpRequest):
    user, dish = get_user_and_obj(request)
    user.collected_dishes.remove(dish)
    return success_response({
        "id": user.id,
        "dish_id": dish.id,
    })


# 查询收藏的菜品
def user_lookup_dish(request: HttpRequest):
    user, dish = get_user_and_obj(request)
    if dish is None:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '菜品不存在')
    else:
        return success_response({
            "id": user.id,
            "dishes": user.collected_dishes,
        })


# 查询收藏的餐馆
def user_lookup_restaurant(request: HttpRequest):
    user, restaurant = get_user_and_obj(request)
    if restaurant is None:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '餐馆不存在')
    else:
        return success_response({
            "id": user.id,
            "dishes": user.collected_restaurants,
        })


def user_lookup_comment(request: HttpRequest):
    user, comment = get_user_and_obj(request)
    if comment is None:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '评论不存在')
    else:
        return success_response({
            "id": user.id,
            "dishes": user.collected_comments,
        })
