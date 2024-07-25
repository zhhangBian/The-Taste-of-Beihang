from django.http import HttpRequest
from django.views.decorators.http import require_GET

from application.dish.models import Dish
from application.utils.response import *


@response_wrapper
@require_GET
def get_dish_basics(request: HttpRequest, dish_name: str):
    dishes = Dish.objects.filter(name=dish_name)
    if not dishes.exists():
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '菜品不存在')

    dishes_basics = [
        {
            "name": dish.name,
            "image": dish.image,
            "address": dish.address,

            "prices": dish.price,
            "description": dish.description,
            "overall_rating": dish.overall_rating,
            "flavor_rating": dish.flavor_rating,
            "waiting_time": dish.waiting_time,

            "restaurant_name": dish.restaurant_name,
        } for dish in dishes
    ]

    return success_response({
        "dishes_count": len(dishes),
        "dishes_info": dishes_basics,
    })


@response_wrapper
@require_GET
def get_detail_info(request: HttpRequest, dish_name: str):
    dishes = Dish.objects.filter(name=dish_name)
    if not dishes.exists():
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '菜品不存在')

    dishes_detail = [
        {
            "name": dish.name,
            "image": dish.image,
            "address": dish.address,
            "overall_rating": dish.overall_rating,
            "price": dish.price,
            "description": dish.description,
            "flavor_rating": dish.flavor_rating,
            "waiting_time": dish.waiting_time,
        } for dish in dishes
    ]

    return success_response({
        "dishes_count": len(dishes),
        "dishes_info": dishes_detail,
    })
