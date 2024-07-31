from django.urls import path

from .api import *

urlpatterns = [
    path('check-login-status', check_login_status),

    path('send-captcha', send_captcha),
    path('change-email', change_email),

    path('login/', user_login),
    path('logout/', user_logout),
    path('signup/', user_signup),
    path('change-password/', change_password),
    path('forget-password/', forget_password),
    path('update-user/', update_user),
    path('update-avatar/', update_avatar),

    path('upload-img/', upload_img),

    path('get-user-info/', get_user_info),
    path('info/<int:user_id>/', get_user_info_by_id),
    path('get-user-detail/', get_user_detail),

    path('get-user-comments', get_user_comments),
    path('get-user-comments-by-id/<int:user_id>', get_user_comments_by_id),

    path('add-record/', add_record),
    path('modify-record/', modify_record),
    path('delete-record/', delete_record),
    path('get-records/', get_records),
    path('get-statics/', get_statics),

    path('create-comment/', creat_comment),

    path('collect-comment/', collect_comment),
    path('collect-restaurant/', collect_restaurant),
    path('collect-dish/', collect_dish),
    path('discollect-comment/', discollect_comment),
    path('discollect-restaurant/', discollect_restaurant),
    path('discollect-dish/', discollect_dish),
    path('get-collected-dishes/', get_collected_dishes),
    path('get-collected-restaurants/', get_collected_restaurants),
    path('get-collected-comments/', get_collected_comments),
]
