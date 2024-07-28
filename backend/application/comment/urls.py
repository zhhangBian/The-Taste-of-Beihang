from django.urls import path

from .api import *

urlpatterns = [
    path('get-comment-basics', get_comment_basics),
    path('create-comment', creat_comment),
    path('agree-comment', agree_comment),

    path('search-comment', search_comment),
]
