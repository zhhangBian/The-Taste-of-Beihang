import random
import re

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest
from django.utils import timezone
from django.views.decorators.http import require_POST, require_GET, require_http_methods

from restaurant.models import Restaurant
from users.models import User
from comment.models import Comment
from utils.data_process import parse_data
from utils.response import *

places = ["学一", "学二", "学三", "学四", "学五", "学六", "美食苑", "其他"]
dishes = ["麻辣香锅", "猪脚饭", "兰州拉面", "黄焖鸡米饭", "汉堡", "", "淄博烧烤", "铁板烧", "茶香鸡"]



