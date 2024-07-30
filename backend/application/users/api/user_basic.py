# 代表了用户的基本接口
import json
import os

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.db.models import Count
from django.http import HttpRequest
from django.views.decorators.http import require_POST, require_GET

from .email import varify_captcha
from ..models import User
from ...comment.models import Comment
from ...dish.models import Dish
from ...record.models.record import Record
from ...utils.response import *

MAGIC_ID = 114514
login_id = MAGIC_ID

# 导入用于装饰器修复技术的包

name_not_allow = ['default', 'delete']
default_avatar = "https://pigkiller-011955-1319328397.cos.ap-beijing.myqcloud.com/img/202407241830349.avif"


@response_wrapper
@require_GET
def check_login_status(request: HttpRequest):
    global login_id

    if login_id != MAGIC_ID:
        return success_response({
            "message": "已登录"
        })
    else:
        return fail_response(ErrorCode.UNAUTHORIZED_ERROR, "还没有登录")


# 用户登录
@response_wrapper
@require_POST
def user_login(request: HttpRequest):
    body = json.loads(request.body.decode('utf-8'))
    username = body.get('username')
    password = body.get('password')
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

    if user:
        login(request, user)

        request.session['is_login'] = True
        request.session['user_id'] = user.id
        request.session['username'] = user.username

        global login_id
        login_id = user.id
        print("login, id to " + str(login_id))
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
    request.session.pop('is_login', None)
    request.session.pop('username', None)
    request.session.pop('user_id', None)
    logout(request)

    global login_id
    login_id = MAGIC_ID
    return success_response({
        "message": "退出成功"
    })


@response_wrapper
@require_POST
def get_user_id(request):
    global login_id
    user = User.objects.filter(id=login_id).first()
    return success_response({
        "user_id": login_id,
        "username": user.username,
    })


# 用户注册
@response_wrapper
@require_POST
def user_signup(request: HttpRequest):
    if request.session.get('is_login', None):
        return success_response({
            "message": "已经登录"
        })
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
    user = User.objects.create_user(username=username,
                                    email=email,
                                    password=password)
    user.save()

    return success_response({
        "message": "注册成功"
    })


# 修改密码
@response_wrapper
@require_POST
def change_password(request: HttpRequest):
    id = login_id
    user = User.objects.filter(id=id).first()

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
    global login_id
    print("now login id is " + str(login_id))
    my_user = User.objects.filter(id=login_id).first()

    body = json.loads(request.body.decode('utf-8'))
    name = body.get('name')
    motto = body.get('motto')
    school = body.get('school')

    if name in name_not_allow:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, '非法取名')
    elif name:
        my_user.name = name
    if motto:
        my_user.motto = motto
    if school:
        my_user.school = school

    my_user.save()
    print("update, login id is " + str(login_id))
    return success_response({"message": "用户资料更新成功"})


@response_wrapper
@require_POST
def update_avatar(request):
    global login_id
    my_user = User.objects.filter(id=login_id).first()

    file = request.FILES.get('file')
    file_path = os.path.join("../../../static", file.name)
    with open(file_path, 'wb+') as f:
        f.write(file.read())
        f.close()
    # url = upload("../../../static" + file.name, file.anme)
    return success_response({
        "avatar": 1,
        "message": "上传成功",
    })


@response_wrapper
@require_GET
def get_user_info(request):
    global login_id
    print(login_id)
    my_user = User.objects.filter(id=login_id).first()
    return success_response({
        "id": my_user.id,
        "username": my_user.username,
        "name": my_user.name,
        "avatar": my_user.avatar,
        "motto": my_user.motto,
    })


@response_wrapper
@require_GET
def get_user_info_by_id(request: HttpRequest, id: int):
    user = User.objects.filter(id=id).first()

    return success_response({
        "id": user.id,
        "username": user.username,
        "name": user.name,
        "email": user.email,
        "school": user.school,

        "motto": user.motto,
        "avatar": user.avatar,
    })


@response_wrapper
@require_GET
def get_user_detail(request: HttpRequest):
    global login_id
    my_user = User.objects.filter(id=login_id).first()

    return success_response({
        "id": my_user.id,
        "username": my_user.username,
        "name": my_user.name,
        "email": my_user.email,
        "school": my_user.school,

        "motto": my_user.motto,
        "avatar": my_user.avatar,
    })


@response_wrapper
@require_POST
def add_comment(request: HttpRequest):
    global login_id
    user = User.objects.filter(id=login_id).first()

    body = json.loads(request.body.decode('utf-8')).get('params')
    title = body.get('title', '默认标题')
    content = body.get('content', '空空如也')
    # TODO：图片问题
    # image = ...
    dish_name = body.get('dish_name', '默认')
    restaurant_name = body.get('restaurant', '默认')

    grade = float(body.get('grade', '5'))
    price = float(body.get('price', '20'))
    if price < 0 or price > 9999:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "价格不合理！")
    flavour = float(body.get('flavour', '5'))
    waiting_time = float(body.get('waiting_time', '60'))

    author_id = 0
    if not user.is_anonymous:
        author_id = user.id

    if Dish.objects.filter(name=dish_name).exists():
        dish = Dish.objects.filter(name=dish_name).first()
        comment = Comment(title=title,
                          content=content,

                          grade=grade,
                          price=price,
                          flavour=flavour,
                          waiting_time=waiting_time,

                          restaurant_name=restaurant_name,
                          dish_name=dish_name,
                          author_id=author_id)
        comment.save()
        dish.comments.add(comment)
        if not user.is_anonymous:
            user.comments.add(comment)
            user.save()
        return success_response({"message": "创建成功！", "title": comment.title})
    else:
        return fail_response(ErrorCode.INVALID_REQUEST_ARGUMENT_ERROR, "菜品不存在！")


@response_wrapper
@require_POST
def add_record(request: HttpRequest):
    global login_id
    my_user = User.objects.filter(id=login_id).first()

    body = json.loads(request.body.decode('utf-8'))
    print(body)
    time = body.get('time')
    dish_name = body.get('dish_name')
    restaurant_name = body.get('restaurant_name')
    price = float(body.get('price'))

    record = Record(dish_name=dish_name,
                    time=time,
                    restaurant_name=restaurant_name,
                    price=price)
    record.save()
    my_user.records.add(record)
    my_user.save()
    print("add record, login id is " + str(login_id))
    return success_response({
        "id": record.id,
        "message": "添加用餐记录成功",
    })


@response_wrapper
@require_POST
def modify_record(request: HttpRequest):
    global login_id
    my_user = User.objects.filter(id=login_id).first()

    body = json.loads(request.body.decode('utf-8'))
    record_id = body.get('record_id', '')
    record = Record.objects.filter(id=record_id).first()

    time = body.get('time', '')
    dish_name = body.get('dish_name', '')
    restaurant_name = body.get('restaurant_name')
    price = float(body.get('price', 0))

    if time:
        record.time = time
    if dish_name:
        record.dish_name = dish_name
    if restaurant_name:
        record.restaurant_name = restaurant_name
    if price:
        record.price = price
    record.save()
    my_user.save()
    print("modify record, login id is " + str(login_id))
    return success_response({
        "message": "修改用餐记录成功",
    })


@response_wrapper
@require_POST
def delete_record(request: HttpRequest):
    global login_id
    my_user = User.objects.filter(id=login_id).first()

    body = json.loads(request.body.decode('utf-8'))
    record_id = int(body.get('record_id'))
    my_user.records.remove(Record.objects.get(id=record_id))
    my_user.save()
    print("delete record, login id is " + str(login_id))
    return success_response({
        "message": "删除用餐记录成功",
    })


@response_wrapper
@require_GET
def get_records(request: HttpRequest):
    global login_id
    my_user = User.objects.filter(id=login_id).first()

    record_info_list = []
    records = list(my_user.records.all())
    record_cnt = len(records)
    price_sum = 0

    # restaurant_frequencies = my_user.records.all().values('restaurant__name').annotate(
    #     freq=Count('restaurant__name')).order_by('freq')
    #
    # # 转换餐馆频次统计结果为字典形式，以便于展示
    # restaurant_freq_dict = {item['restaurant__name']: item['freq'] for item in restaurant_frequencies}

    for record in records:
        price_sum += record.price
        record_info_list.append(({
            "id": record.id,
            "time": record.time,
            "dish_name": record.dish_name,
            "restaurant_name": record.restaurant_name,
            "price": record.price,
        }))

    return success_response({
        "records": record_info_list,
        "records_count": record_cnt,
        # "price_mean": price_sum / record_cnt,
        # "freq_dict": restaurant_freq_dict,
    })
