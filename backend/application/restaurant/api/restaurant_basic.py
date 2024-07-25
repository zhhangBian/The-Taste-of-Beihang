from ..models import Restaurant
from django.http import HttpRequest
from django.utils import timezone
from django.views.decorators.http import require_POST, require_GET

from utils.response import *


@response_wrapper
@require_POST
def update_image(request: HttpRequest, restaurant_name: str):
    restart = Restaurant.objects.get(name=restaurant_name)
    if restart is None:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '餐馆不存在')

    img = request.FILES.getlist('image')[0] if len(request.FILES.getlist('image')) > 0 else None
    if img is not None:
        img.name = restart.name + str(timezone.now()) + '.png'
        restart.img = img
    restart.save()
    return success_response({"message": "图片修改成功！"})


@response_wrapper
@require_GET
def get_basic_info(request: HttpRequest, restaurant_name: str):
    restart = Restaurant.objects.get(name=restaurant_name)
    if restart is None:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '餐馆不存在')
    # return restaurant info
    return success_response({
        "name": restart.name,
        "img": restart.img,
        "description": restart.description,
        "detail_addr": restart.detail_addr,
    })
