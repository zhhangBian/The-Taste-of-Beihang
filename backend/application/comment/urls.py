from django.urls import path

from .api import *

urlpatterns = [
    path('get-comment-basics/<int:comment_id>', get_comment_basics),
    path('create-comment', creat_comment),
    path('agree-comment/<int:comment_id>', agree_comment),

    path('create-comment', create_comment),

    path('search-comment', search_comment),
    path('search-comment-restaurant', search_comment_restaurant),
]
