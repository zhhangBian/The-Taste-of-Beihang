import json

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from application.dish.models import Dish
from application.utils.response import *


@response_wrapper
@require_POST
def creat_dish(request):
    user = request.user

    body = json.loads(request.body.decode('utf-8'))
    dish_name = body.get('dish_name', '默认名称')
    # TODO: image
    restaurant_name = body.get('restaurant_name', '任何餐厅')
    address = body.get('dish_address', '任何地方')
    description = body.get('description', '')

    dish = Dish(name=dish_name, address=address, description=description)
    dish.save()
    return success_response({"message": "创建成功！"})


@response_wrapper
@require_POST
def get_dish(request):
    user = request.user

    body = json.loads(request.body.decode('utf-8'))
    restaurant_name = body.get('restaurant_name')
    dish_name = body.get('dish_name')

    dish = Dish.objects.get(restaurant_name=restaurant_name, name=dish_name)
    return success_response({
        "id": dish.id,
        "name": dish.name,
        "image": dish.image,

        "restaurant_name": dish.restaurant_name,
        "address": dish.address,

        "description": dish.description,

        "prices": dish.price,
        "overall_rating": dish.overall_rating,
        "flavor_rating": dish.flavor_rating,
        "waiting_time": dish.waiting_time,
    })
