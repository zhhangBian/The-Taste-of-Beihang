from django.views.decorators.http import require_POST

from dish.models import Dish
from restaurant.models import Restaurant
from application.utils.data_process import parse_data
from utils.response import fail_response, ErrorCode, success_response, response_wrapper


@response_wrapper
@require_POST
def creat_dish(request):
    user = request.user
    post_data = parse_data(request)
    name = post_data.get('name')

    if Restaurant.objects.filter(name=name).exists():
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "餐厅已存在！")
    restaurant = Restaurant(name=name, creator=user)

    restaurant.save()
    return success_response({"message": "创建成功！"})


@response_wrapper
@require_POST
def get_dish(request):
    user = request.user
    post_data = parse_data(request)

    restaurant_name = post_data.get('restaurant_name')
    restaurant = Restaurant.objects.get(name=restaurant_name)
    dish_name = post_data.get('dish_name')

    dish = Dish.objects.get(restaurant=restaurant, name=dish_name)
    return success_response({
        "name": dish.name,
        "image": dish.image,
        "address": dish.address,
        "prices": dish.price,
        "description": dish.description,
        "overall_rating": dish.overall_rating,
        "flavor_rating": dish.flavor_rating,
        "waiting_time": dish.waiting_time,
    })
