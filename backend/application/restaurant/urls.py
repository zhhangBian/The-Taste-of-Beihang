from django.urls import path

from .api import *

urlpatterns = [
    path('get-basic-info', get_basic_info),
]