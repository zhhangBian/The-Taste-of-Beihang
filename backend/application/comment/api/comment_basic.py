import json

from django.http import HttpRequest
from django.views.decorators.http import require_GET, require_POST

from ..models import Comment
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
