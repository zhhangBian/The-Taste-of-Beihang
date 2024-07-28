import json

from django.http import HttpRequest
from django.views.decorators.http import require_GET

from application.dish.models import Dish
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
