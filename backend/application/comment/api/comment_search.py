# 获取评论的集合
import difflib
import json

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from application.comment.models import Comment
from application.dish.models import Dish
from application.utils.response import response_wrapper, success_response


def serialize_comments(comments) -> list:
    """
    获取评论的信息序列
    """
    comments_list = []

    for comment in comments:
        dish = Dish.objects.filter(name=comment.dish_name).first()
        # print(dish.id)
        comment_dict = {
            'id': comment.id,
            'title': comment.title,
            'content': comment.content,
            'date': comment.date.strftime('%Y-%m-%d %H:%M:%S'),  # 格式化日期
            'image': comment.image,

            'grade': comment.grade,
            'price': comment.price,
            'flavour': comment.flavour,
            'waiting_time': comment.waiting_time,

            'restaurant_name': comment.restaurant_name,
            'dish_name': comment.dish_name,
            'dish_id': dish.id,
            'author_id': comment.author_id,
        }
        comments_list.append(comment_dict)

    return comments_list


def matches_search(comment, search_string):
    return (difflib.SequenceMatcher(None, comment.title, search_string).ratio() > 0.3) or (
            comment.title in search_string) or (search_string in comment.title)


@response_wrapper
@require_POST
def search_comment(request):
    body = json.loads(request.body.decode('utf-8'))
    search_string = body.get('search', '')
    restaurant_name = body.get('restaurant_name', '全选')
    dish_name = body.get('dish_name', '全选')

    print(search_string)
    print(restaurant_name)
    print(dish_name)

    comments = Comment.objects.all()

    if restaurant_name != '全选':
        comments = comments.filter(restaurant_name=restaurant_name)
    if dish_name != '所有菜品':
        comments = comments.filter(dish_name=dish_name)

    comments_fit = []
    for comment in comments:
        if matches_search(comment, search_string):
            comments_fit.append(comment)
    comments_fit_serialized = serialize_comments(comments_fit)

    return success_response({
        "comments": comments_fit_serialized,
        "comments_count": len(comments_fit_serialized)
    })
