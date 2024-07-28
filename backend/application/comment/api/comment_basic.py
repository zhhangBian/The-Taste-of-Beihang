import json

from django.http import HttpRequest
from django.views.decorators.http import require_GET, require_POST

from ..models import Comment
from ...dish.models import Dish
from ...users.api import User
from ...utils.response import response_wrapper, fail_response, ErrorCode, success_response


@response_wrapper
@require_GET
def get_comment_basics(request: HttpRequest):
    body = json.loads(request.body.decode('utf-8'))
    comment_id = body.get('comment_id', '')

    comment = Comment.objects.get(id=comment_id)
    if comment is None:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '评论不存在')
    author = User.objects.get(id=comment.author_id)
    author_name = author.name
    return success_response({
        "title": comment.title,
        "content": comment.content,
        "date": comment.date,
        "image": comment.image,

        "grade": comment.grade,
        "flavour": comment.flavour,
        "price": comment.price,
        "waiting_time": comment.waiting_time,

        "author": author_name,
        "dish": comment.dish_name,
        "restaurant": comment.restaurant_name
    })


@response_wrapper
@require_POST
def creat_comment(request):
    user = request.user

    body = json.loads(request.body.decode('utf-8'))
    title = body.get('title', '默认标题')
    content = body.get('content', '空空如也')
    # TODO：图片问题
    # image = ...
    dish_name = body.get('dish_name', '默认')
    restaurant_name = body.get('restaurant', '默认')

    grade = body.get('grade', '5')
    if grade not in [0, 1, 2, 3, 4, 5]:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "评分不合法！")
    price = body.get('price', '20')
    if price < 0 or price > 9999:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "价格不合理！")
    flavour = body.get('flavour', '5')
    waiting_time = body.get('waiting_time', '60')

    if Dish.objects.filter(name=dish_name).exists():
        dish = Dish.objects.filter(name=dish_name)
        comment = Comment(title=title,
                          content=content,

                          grade=grade,
                          price=price,
                          flavour=flavour,
                          waiting_time=waiting_time,

                          dish_name=dish_name,
                          restaurant_name=restaurant_name,
                          author_id=user.id)
        comment.save()
        dish.comments.add(comment)
        return success_response({"message": "创建成功！", "title": comment.title})
    else:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "菜品不存在！")


@response_wrapper
@require_POST
def agree_comment(request: HttpRequest):
    body = json.loads(request.body.decode('utf-8'))
    comment_id = body.get('comment_id', '')
    comment = Comment.objects.get(id=comment_id)
    user = request.user
    if comment is None:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "评论不存在")
    if user in comment.agrees.all():
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "已点赞")

    comment.agree_count.add(1)
    comment.agree_authors.add(user)
    return success_response({"message": "点赞成功！"})
