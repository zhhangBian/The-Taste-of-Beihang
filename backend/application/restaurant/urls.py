from django.urls import path

from .api import *

urlpatterns = [
    path('update-image/<str:restaurant_name>', update_image),
    path('get-basic-info/<str:restaurant_name>', get_basic_info),
]