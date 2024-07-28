# 代表了用户的基本接口


from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from .auth import *
from .email import varify_captcha
from ..models import User
from ...utils.response import *

name_not_allow = ['default', 'delete']
User = get_user_model()


# 用户登录
@response_wrapper
@require_POST
def user_login(request: HttpRequest):
    username = request.GET.get('username')
    password = request.GET.get('password')
    # 使用Django的authenticate函数验证用户名和密码
    user = authenticate(username=username, password=password)

    # 通过查询邮箱找到对应的用户
    if user is None and '@' in username:
        # 使用邮箱登录，查询email相等的用户
        tmp_user = User.objects.filter(email=username).first()
        if tmp_user is None:
            return fail_response(ErrorCode.CANNOT_LOGIN_ERROR, "用户名或邮箱不存在！")
        username = tmp_user.username
        user = authenticate(username=username, password=password)

    if user is not None:
        request.session['is_login'] = True
        request.session['user_id'] = user.id
        request.session['username'] = user.username
        return success_response({
            "message": "登录成功"
        })
    elif User.objects.filter(username=username).exists():
        return fail_response(ErrorCode.CANNOT_LOGIN_ERROR, "密码错误！")
    else:
        return fail_response(ErrorCode.CANNOT_LOGIN_ERROR, "用户名或邮箱不存在！")


@response_wrapper
@require_GET
def user_logoff(request):
    # 如果不是登陆状态，无法登出
    if request.session.get('is_login'):
        request.session.flush()
    return redirect('/login/')


# 用户注册
@response_wrapper
@require_POST
def user_signup(request: HttpRequest):
    
    username = request.GET('username')
    password = request.GET('password')
    email = request.GET('email')
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
    User.objects.create_user(username=username, email=email, password=password)

    return success_response({'message': '注册成功'})


# 修改密码
@response_wrapper
@require_POST
def change_password(request: HttpRequest):
    
    old_password = request.GET('old_password')
    new_password = request.GET('new_password')

    # 使用Django的authenticate函数验证用户名和密码
    user = authenticate(username=request.user.username, password=old_password)
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
    
    email = request.GET('email')
    captcha = request.GET('captcha')
    new_password = request.GET('password')
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
    user = request.user
    # 获取数据
    
    username = request.GET('username')
    motto = request.GET('motto')

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
    user = request.user

    return success_response({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "avatar": user.avatar,
        "motto": user.motto,
    })


@response_wrapper
@require_GET
def get_user_info_by_id(request: HttpRequest, user_id: int):
    target_user = User.objects.filter(id=user_id).first()
    if target_user is None:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "用户不存在！")

    return success_response({
        "id": target_user.id,
        "username": target_user.username,
        "email": target_user.email,
        "avatar": target_user.avatar.url,
        "motto": target_user,
    })
