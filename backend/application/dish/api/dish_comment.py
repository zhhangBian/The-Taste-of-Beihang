from django.views.decorators.http import require_GET

from application.comment.models import Comment
from application.dish.models import Dish
from application.users.api import User
from application.utils.data_process import parse_data
from application.utils.response import *


@response_wrapper
@require_GET
def get_dish_comments(request):
    post_data = parse_data(request)

    address = post_data.get("dish_address")
    name = post_data.get("dish_name")

    dish = Dish.objects.get(name=name, address=address)
    comments_count = dish.dish_comments.count()

    comments_list = []
    dish_comments = Comment.objects.filter(dish_name=dish.name)

    grade_sum = 0
    price_sum = 0
    flavor_sum = 0
    waiting_sum = 0
    n = len(dish_comments)

    for comment in dish_comments:
        author_id = comment.author_id
        author = User.objects.get(id=author_id)

        grade_sum += comment.grade
        price_sum += comment.price
        flavor_sum += comment.flavour
        waiting_sum += comment.waiting_time

        comment_dict = {
            'title': comment.title,
            'content': comment.content,
            'date': comment.date,
            'image': comment.image,

            'grade': comment.grade,
            'price': comment.price,
            'flavor': comment.flavour,
            'waiting_time': comment.waiting_time,

            'author_id': comment.author_id,
            'avatar': author.avatar,
            'name': author.username
        }
        comments_list.append(comment_dict)

    grade = grade_sum / n
    price = price_sum / n
    flavor = flavor_sum / n
    waiting_time = waiting_sum / n

    return success_response({
        "comments_count": comments_count,
        "comments_list": comments_list,
        "grade": grade,
        "price": price,
        "flavor": flavor,
        "waiting_time": waiting_time
    })
