from django.http import HttpRequest
from django.views.decorators.http import require_GET

from application.users.models import User
from application.utils.response import *


# 获取评论的集合
def serialize_comments(user: 'User') -> list:
    comments_list = []
    user_comments = user.comments.all()

    for comment in user_comments:
        comment_dict = {
            'title': comment.title,
            'content': comment.content,
            'date': comment.date.strftime('%Y-%m-%d %H:%M:%S'),  # 格式化日期
            'image': comment.image,

            'grade': comment.grade,
            'price': comment.price,
            'waiting_time': comment.waiting_time,

            'author_id': comment.author_id,
            'dish_name': comment.dish_name,
            'restaurant_name': comment.restaurant_name,
        }
        comments_list.append(comment_dict)

    return comments_list


@response_wrapper
@require_GET
def get_user_comments(request):
    user = request.user
    comments_count = user.comments.count()

    return success_response({
        "comments_count": comments_count,
        "comments_list": serialize_comments(user),
    })


@response_wrapper
@require_GET
def get_user_comments_by_id(request: HttpRequest, user_id: int):
    target_user = User.objects.filter(id=user_id).first()
    if target_user is None:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "用户不存在！")

    comments_count = target_user.comments.count()

    return success_response({
        "comments_count": comments_count,
        "comments_list": serialize_comments(target_user),
    })
