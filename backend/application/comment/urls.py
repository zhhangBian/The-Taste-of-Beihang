from django.urls import path

from .api import *

urlpatterns = [
    path('get-comment-basics', get_comment_basics),
    path('agree-comment', agree_comment),

    path('search-comment', search_comment),
    path('get-llm-answer', get_llm_answer),
]
