# 代表了用户的基本接口
import json

from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views.decorators.http import require_POST, require_GET

from .email import varify_captcha
from ..models import User
from ...utils.response import *

name_not_allow = ['default', 'delete']

login_id = 0


@response_wrapper
@require_GET
def check_login_status(request: HttpRequest):
    print(114514)
    if request.user.is_authenticated:
        return success_response({"login_status": 1})
    else:
        return success_response({"login_status": 0})


# 用户登录
@response_wrapper
@require_POST
def user_login(request: HttpRequest):
    body = json.loads(request.body.decode('utf-8'))
    username = body.get('username')
    password = body.get('password')
    # 使用Django的authenticate函数验证用户名和密码
    user = authenticate(username=username, password=password)

    global login_id
    login_id = user.id
    print("login " + str(login_id))

    # 通过查询邮箱找到对应的用户
    if user is None and '@' in username:
        # 使用邮箱登录，查询email相等的用户
        tmp_user = User.objects.filter(email=username).first()
        if tmp_user is None:
            return fail_response(ErrorCode.CANNOT_LOGIN_ERROR, "用户名或邮箱不存在！")
        username = tmp_user.username
        user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        print("login " + str(request.user.is_authenticated))
        return success_response({
            "message": "登录成功"
        })
    elif User.objects.filter(username=username).exists():
        # 密码错误
        return fail_response(ErrorCode.CANNOT_LOGIN_ERROR, "密码错误！")
    else:
        # 登录失败
        return fail_response(ErrorCode.CANNOT_LOGIN_ERROR, "用户名或邮箱不存在！")


@response_wrapper
@require_GET
def user_logout(request):
    auth.logout(request)
    return redirect('/login/')


# 用户注册
@response_wrapper
@require_POST
def user_signup(request: HttpRequest):
    body = json.loads(request.body.decode('utf-8'))
    username = body.get('username')
    password = body.get('password')
    email = body.get('email')
    # TODO：对于邮箱发送验证码的支持
    # captcha = request.GET('captcha')

    # 检查是否有字段为空
    if username is None or password is None or email is None:
        return fail_response(ErrorCode.REQUIRED_ARG_IS_NULL_ERROR, '内容未填写完整')

    # 检查用户名是否已存在
    if User.objects.filter(username=username).exists():
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '用户名已存在')
    if username in name_not_allow:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '非法取名')
    if User.objects.filter(email=email).exists():
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "邮箱已注册")
    if password == '':
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "密码不能为空")
    # 验证验证码
    # if not varify_captcha(email, captcha):
    #     return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "验证码错误")

    # 创建新用户
    User.objects.create_user(username=username,
                             email=email,
                             password=password)

    return success_response({'message': '注册成功'})


# 修改密码
@response_wrapper
@require_POST
def change_password(request: HttpRequest):
    global login_id
    user = User.objects.filter(id=login_id).first()

    body = json.loads(request.body.decode('utf-8'))
    old_password = body.get('old_password')
    new_password = body.get('new_password')

    # 使用Django的authenticate函数验证用户名和密码
    user = authenticate(username=user.username, password=old_password)
    if user is not None:
        # 修改密码
        user.password = make_password(new_password)
        user.save()
        return success_response({'message': '密码修改成功'})
    else:
        # 登录失败
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "原密码错误")


# 忘记密码：修改密码的翻版
# TODO：对邮件的支持
@response_wrapper
@require_POST
def forget_password(request: HttpRequest):
    body = json.loads(request.body.decode('utf-8'))
    email = body.get('email')
    captcha = body.get('captcha')
    new_password = body.get('password')

    user = User.objects.filter(email=email).first()
    if user is None:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "邮箱未注册")
    if varify_captcha(email, captcha):
        user.password = make_password(new_password)
        user.save()
        return success_response({"message": "验证码正确，密码已修改"})
    else:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "验证码错误")


@response_wrapper
@require_POST
def update_user(request: HttpRequest):
    # 获取用户
    global login_id
    user = User.objects.get(id=login_id)

    body = json.loads(request.body.decode('utf-8'))
    username = body.get('username')
    motto = body.get('motto')

    # 检查用户名是否已存在
    if username and User.objects.filter(username=username).exists():
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '用户名已存在')
    elif username in name_not_allow:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '非法取名')
    elif username:
        user.username = username

    # 检查个性签名是否为空
    if motto:
        user.motto = motto

    # 更新用户
    user.save()
    return success_response({"message": "更新成功"})


@response_wrapper
@require_GET
def get_user_info(request):
    global login_id
    print("get " + str(login_id))
    my_user = User.objects.filter(id=login_id).first()

    if login_id == 0:
        return success_response(({"message":"quick login"}))
    return success_response({
        "id": my_user.id,
        "username": my_user.username,
        "avatar": my_user.avatar,
    })


@response_wrapper
@require_GET
def get_user_info_by_id(request: HttpRequest, id: int):
    user = User.objects.filter(id=id).first()

    return success_response({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "school": user.school,

        "motto": user.motto,
        "avatar": user.avatar,
    })
