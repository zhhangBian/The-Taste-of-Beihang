from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET

from application.dish.models import Dish
from application.users.api import User
from application.utils.response import *


@response_wrapper
@require_GET
def get_dish_comments(request):
    restaurant_name = request.GET.get("restaurant_name")
    dish_name = request.GET.get("dish_name")

    print(restaurant_name)
    print(dish_name)

    dish = Dish.objects.get(name=dish_name, address=restaurant_name)
    dish_comments = dish.comments.all()

    comments_count = dish.dish_comments.count()
    comments_list = []

    grade_sum = 0
    price_sum = 0
    flavor_sum = 0
    waiting_sum = 0

    for comment in dish_comments:
        author_id = comment.author_id
        author = User.objects.get(id=author_id)
        author_name = author.name

        grade_sum += comment.grade
        price_sum += comment.price
        flavor_sum += comment.flavour
        waiting_sum += comment.waiting_time

        comment_dict = {
            'id': comment.id,
            'title': comment.title,
            'content': comment.content,
            'date': comment.date,
            'image': comment.image,

            'grade': comment.grade,
            'price': comment.price,
            'flavor': comment.flavour,
            'waiting_time': comment.waiting_time,

            'restaurant_name': comment.restaurant_name,
            'dish_name': comment.dish_name,
            'author_name': author_name
        }
        comments_list.append(comment_dict)

    grade = grade_sum / comments_count
    price = price_sum / comments_count
    flavor = flavor_sum / comments_count
    waiting_time = waiting_sum / comments_count

    return success_response({
        "comments_count": comments_count,
        "comments_list": comments_list,
        "grade": grade,
        "price": price,
        "flavor": flavor,
        "waiting_time": waiting_time
    })
