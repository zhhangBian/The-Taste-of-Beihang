from django.views.decorators.http import require_POST

from application.dish.models import Dish
from application.restaurant.models import Restaurant
from application.utils.response import *


@response_wrapper
@require_POST
def creat_dish(request):
    user = request.user
    
    name = request.GET('name')

    if Restaurant.objects.filter(name=name).exists():
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "餐厅已存在！")
    restaurant = Restaurant(name=name, creator=user)

    restaurant.save()
    return success_response({"message": "创建成功！"})


@response_wrapper
@require_POST
def get_dish(request):
    user = request.user
    

    restaurant_name = request.GET('restaurant_name')
    dish_name = request.GET('dish_name')

    dish = Dish.objects.get(restaurant_name=restaurant_name, name=dish_name)
    return success_response({
        "name": dish.name,
        "image": dish.image,
        "address": dish.address,

        "prices": dish.price,
        "description": dish.description,
        "overall_rating": dish.overall_rating,
        "flavor_rating": dish.flavor_rating,
        "waiting_time": dish.waiting_time,

        "restaurant_name": dish.restaurant_name,
    })
