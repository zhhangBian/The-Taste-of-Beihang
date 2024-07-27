from django.http import HttpRequest
from django.views.decorators.http import require_GET, require_POST


from ..models import Comment
from ...dish.models import Dish
from ...utils.response import response_wrapper, fail_response, ErrorCode, success_response


@response_wrapper
@require_GET
def get_comment_basics(request: HttpRequest, comment_id: int):
    comment = Comment.objects.get(id=comment_id)
    if comment is None:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '评论不存在')
    return success_response({
        "grade": comment.grade,
        "flavour": comment.flavour,
        "price": comment.price,
        "waiting_time": comment.waiting_time,
        "content": comment.content,
        "date": comment.date,
        "author": comment.author,
    })


@response_wrapper
@require_POST
def creat_comment(request):
    user = request.user

    dish_name = request.GET('dish_name')
    title = request.GET('title')
    content = request.GET('content')
    grade = request.GET('grade')
    if grade not in [0, 1, 2, 3, 4, 5]:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "评分不合法！")
    price = request.GET('price')
    if price < 0 or price > 9999:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "价格不合理！")
    flavour = request.GET('flavour')
    waiting_time = request.GET('waiting_time')

    if Dish.objects.filter(name=dish_name).exists():
        dish = Dish.objects.filter(name=dish_name)
        comment = Comment(title=title, content=content, creator=user, grade=grade, avg_price=price, flavour=flavour,
                          waiting_time=waiting_time, dish=dish)
        comment.save()
        return success_response({"message": "创建成功！", "title": comment.title})
    else:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "菜品不存在！")


@response_wrapper
@require_POST
def agree_comment(request: HttpRequest, comment_id: int):
    comment = Comment.objects.get(id=comment_id)
    user = request.user
    if comment is None:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "评论不存在")
    if user in comment.agrees.all():
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "已点赞")

    comment.agree_count.add(1)
    comment.agree_authors.add(user)
    return success_response({"message": "点赞成功！"})
