from django.urls import path

from .api import *

urlpatterns = [
    path('send-email', send_email),
    path('send-captcha', send_captcha),
    path('change-email', change_email),

    path('login/', user_login),
    path('logout/', user_logoff),
    path('signup/', user_signup),
    path('change-password/', change_password),
    path('forget-password/', forget_password),
    path('update-user/', update_user),
    path('get-user-info/', get_user_info),
    path('get-user-info/<int:user_id>/', get_user_info_by_id),

    path('get-user-comments', get_user_comments),
    path('get-user-comments-by-id/<int:user_id>', get_user_comments_by_id),
]
