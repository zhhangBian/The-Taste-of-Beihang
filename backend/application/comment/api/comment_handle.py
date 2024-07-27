from django.views.decorators.http import require_POST

from ..models import Comment
from ...dish.models import Dish
from ...restaurant.models import Restaurant
from ...utils.response import response_wrapper, success_response


@response_wrapper
@require_POST
def create_comment(request):
    user = request.user
    

    # 基本的组织逻辑为：食堂-dish-comment
    restaurant_name = request.GET('restaurant')
    restaurant = Restaurant.objects.get(name=restaurant_name)

    dish_name = request.GET('dish_name')
    dish = Dish.objects.get(name=dish_name, restaurant=restaurant)

    # 创建一个新的评论实例
    comment = Comment(
        title=request.GET('title'),
        content=request.GET('content'),
        # img之后处理
        grade=request.GET('grade'),
        price=request.GET('price'),
        flavour=request.GET('flavour'),
        waiting_time=request.GET('waiting_time'),

        restaurant=restaurant,
        dish=dish,
        author=user,

        agree_count=0,
    )
    comment.save()

    # 重定向到评论列表页面或其他页面
    return success_response({"评论创建成功！"})
