from django.urls import path

from .api import *

urlpatterns = [
    path('get-basic-info/<str:restaurant_name>', get_basic_info),
]