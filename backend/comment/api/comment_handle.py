from django.views.decorators.http import require_POST

from dish.models import Dish
from restaurant.models import Restaurant
from utils.data_process import parse_data
from utils.response import success_response, response_wrapper
from ..models import Comment


@response_wrapper
@require_POST
def create_comment(request):
    user = request.user
    post_data = parse_data(request)

    # 基本的组织逻辑为：食堂-dish-comment
    restaurant_name = post_data.get('restaurant')
    restaurant = Restaurant.objects.get(name=restaurant_name)

    dish_name = post_data.get('dish_name')
    dish = Dish.objects.get(name=dish_name, restaurant=restaurant)

    # 创建一个新的评论实例
    comment = Comment(
        title=post_data.get('title'),
        content=post_data.get('content'),
        # img之后处理
        grade=post_data.get('grade'),
        price=post_data.get('price'),
        flavour=post_data.get('flavour'),
        waiting_time=post_data.get('waiting_time'),

        restaurant=restaurant,
        dish=dish,
        author=user,

        agree_count=0,
    )
    comment.save()

    # 重定向到评论列表页面或其他页面
    return success_response({"评论创建成功！"})
