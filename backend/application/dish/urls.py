from django.urls import path

from .api import *

urlpatterns = [
    path('create-dish', creat_dish),
    path('get-dish', get_dish),

    path('get-dish-comments', get_dish_comments),

    path('get-dish-basics', get_dish_info),

    path('get-dish-recommend', get_dish_recommend)
]
