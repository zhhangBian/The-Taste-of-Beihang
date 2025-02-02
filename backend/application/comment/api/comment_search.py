# 获取评论的集合
import difflib
import json
import random

from django.views.decorators.http import require_POST

from application.comment.models import Comment
from application.dish.models import Dish
from application.utils.llm import getLLMresponse
from application.utils.response import response_wrapper, success_response


def serialize_comments(comments) -> list:
    """
    获取评论的信息序列
    """
    comments_list = []

    for comment in comments:
        dish = Dish.objects.filter(name=comment.dish_name).first()

        comments = Comment.objects.filter(dish_name=dish.name)
        grade_sum = 0
        price_sum = 0
        flavour_sum = 0
        waiting_time_sum = 0

        for comment in comments:
            grade_sum += comment.grade
            price_sum += comment.price
            flavour_sum += comment.flavour
            waiting_time_sum += comment.waiting_time

        n = len(comments)
        grade_mean = grade_sum / n
        price_mean = price_sum / n
        flavour_mean = flavour_sum / n
        waiting_time_mean = waiting_time_sum / n

        # print(dish.id)
        comment_dict = {
            'id': comment.id,
            'title': comment.title,
            'content': comment.content,
            'date': comment.date.strftime('%Y-%m-%d %H:%M:%S'),  # 格式化日期
            'image': comment.image,

            'grade': grade_mean,
            'price': price_mean,
            'flavour': flavour_mean,
            'waiting_time': waiting_time_mean,

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
    random.shuffle(comments_fit)
    comments_fit_serialized = serialize_comments(comments_fit)

    return success_response({
        "comments": comments_fit_serialized,
        "comments_count": len(comments_fit_serialized),
    })


@response_wrapper
@require_POST
def get_llm_answer(request):
    body = json.loads(request.body.decode('utf-8'))
    search_string = body.get('search', '')

    llm_answer = getLLMresponse(search_string)

    print(search_string)
    print(llm_answer)

    return success_response({
        "llm_answer": llm_answer,
    })
