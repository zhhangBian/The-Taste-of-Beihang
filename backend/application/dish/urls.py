from django.urls import path

from .api import *

urlpatterns = [
    path('create-dish', creat_dish),
    path('get-dish', get_dish),

    path('get-dish-comments', get_dish_comments),

    path('get-dish-info', get_dish_info),
    path('detail/<int:id>/', get_dish_info_id),

    path('get-dish-recommend', get_dish_recommend)
]
