import random

from django.http import HttpRequest
from django.views.decorators.http import require_GET

from application.utils.response import *

places = ["学一", "学二", "学三", "学四", "学五", "学六", "美食苑", "其他"]
dishes = ["麻辣香锅", "猪脚饭", "兰州拉面", "黄焖鸡米饭", "汉堡", "", "淄博烧烤", "铁板烧", "茶香鸡"]


@response_wrapper
@require_GET
def get_dish_recommend(request: HttpRequest, dish_name: str):
    place = random.choice(places)
    dish = random.choice(dishes)
    recommendation = "在" + str(place) + "吃" + str(dish)

    return success_response({
        "recommendation": recommendation
    })
