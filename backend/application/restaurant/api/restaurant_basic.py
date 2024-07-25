from django.http import HttpRequest
from django.views.decorators.http import require_GET

from ..models import Restaurant
from ...utils.response import *


@response_wrapper
@require_GET
def get_basic_info(request: HttpRequest, restaurant_name: str):
    restaurant = Restaurant.objects.get(name=restaurant_name)
    if restaurant is None:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '餐馆不存在')
    # return restaurant info
    return success_response({
        "name": restaurant.name,
        "image": restaurant.image,
        "description": restaurant.description,
        "address": restaurant.address,
    })
