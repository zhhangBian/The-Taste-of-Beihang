from django.urls import path

from .api import *

urlpatterns = [
    path('create-dish', creat_dish),
    path('get-dish', get_dish),

    path('get-dish-comments', get_dish_comments),

    path('get-dish-basics/<str:dish_name>', get_dish_basics),
    path('get-detail-info/<str:dish_name>', get_detail_info),

    path('get-dish-recommend', get_dish_recommend)
]
