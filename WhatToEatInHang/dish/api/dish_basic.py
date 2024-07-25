from django.http import HttpRequest
from django.views.decorators.http import require_GET, require_POST

from restaurant.models import Restaurant
from utils.data_process import parse_data
from utils.response import fail_response, ErrorCode, success_response, response_wrapper
from ..models import Dish


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


def get_dish():
    pass
