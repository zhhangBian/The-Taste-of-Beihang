# 代表了和邮件相关的操作
import json
import random

from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail
from django.views.decorators.http import require_POST

from .auth import generate_token
from ..models import User
from ...utils.response import *


@response_wrapper
@require_POST
def send_email(request):
    # 获取数据
    body = json.loads(request.body.decode('utf-8'))
    email = body.get('email')
    content = body.getT('content')
    # 检查邮箱是否已存在
    if email and User.objects.filter(email=email).exists():
        # 生成token
        token = generate_token(email)
        # 发送邮件
        send_mail(content, token, settings.EMAIL_HOST_USER, [email])
        return success_response({"message": "Email sent successfully."})
    else:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "邮箱不存在！")


def varify_captcha(email, captcha):
    entry = cache.get(email)
    return entry == captcha


@response_wrapper
@require_POST
def send_captcha(request):
    body = json.loads(request.body.decode('utf-8'))
    email = body.get('email')

    captcha = '%06d' % random.randint(0, 999999)
    email_title = 'HangEat 验证码'
    email_body = '您的验证码为：' + captcha + '，请在5分钟内输入。'
    send_status = send_mail(email_title, email_body, settings.EMAIL_HOST_USER, [email])
    if send_status:
        cache.set(email, captcha, 300)
        return success_response({"message": "邮件发送成功，可能存在一定的延迟，请耐心等待。"})
    else:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR,
                             "邮件发送失败，请检查邮箱是否正确。")


@response_wrapper
@require_POST
def change_email(request):
    body = json.loads(request.body.decode('utf-8'))
    new_email = body.get('email')
    captcha = body.get('captcha')
    if User.objects.filter(email=new_email).exists():
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "邮箱已注册")
    if varify_captcha(new_email, captcha):
        user = request.user
        user.email = new_email
        user.save()
        return success_response({"message": "邮箱修改成功！"})
    else:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "验证码错误！")
