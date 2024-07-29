import json

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.views.decorators.http import require_GET

from ..models import Restaurant
from ...utils.response import *


@response_wrapper
@require_GET
def get_basic_info(request: HttpRequest):
    body = json.loads(request.body.decode('utf-8'))
    restaurant_name = body.get('restaurant_name', '')

    restaurant = Restaurant.objects.get(name=restaurant_name)
    if restaurant is None:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '餐馆不存在')

    return success_response({
        "name": restaurant.name,
        "image": restaurant.image,
        "description": restaurant.description,
        "address": restaurant.address,
    })
