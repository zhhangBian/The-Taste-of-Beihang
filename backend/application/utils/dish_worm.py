import os
import urllib.request

import django
import requests
from bs4 import BeautifulSoup

from application.utils.pic_upload import upload

# 设置环境变量并初始化 Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WhatToEatInHang.settings')
django.setup()

from application.dish.models import Dish
import random


def generate_random_float(a, b):
    # 可能的整数部分列表
    integers = list(range(a, b))
    # 随机选择一个整数，并构造对应的浮点数（整数+0.5，除了18直接返回）
    chosen_int = random.choice(integers)
    havePointFive = random.choice([True, False])
    if havePointFive:
        return float(f"{chosen_int}.0")
    else:
        return float(f"{chosen_int}.5")


def generate_random_real_float(a, b):
    return round(random.uniform(a, b), 1)


def import_data(data):
    dish, created = Dish.objects.update_or_create(
        name=data['title'],
        image=data['img_url'],

        address=data['location'],
        restaurant_name=data['window'],

        description=data['description'],

        price=generate_random_float(8, 18),
        overall_rating=generate_random_real_float(4, 5),
        flavor_rating=generate_random_real_float(4, 5),
        waiting_time=generate_random_float(0, 2),
    )


# response = requests.get(url)
# response_json = response.json()
# df = pd.json_normalize(response_json, errors='ignore')
#
# df = df.loc[: ['a', 'b']]
#
# conn = sqlite3.connect('wormtest.db')
# df.to_sql('wormtest', conn, if_exists='replace', index=False)
# conn.commit()
# conn.close()


def download_img(url, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.findAll('p', class_='contentFont', string=lambda x: x and x.startswith('#'))

    for title_tag in titles:
        # 查找img元素
        img_tag = title_tag.find_next_sibling('p', class_='contentImage').img
        print(img_tag.get('src'))

        title = str(title_tag.text).replace(" ", "").replace("\t", "").replace("\n", "")
        path = save_dir + '/' + str(title) + '.jpg'
        urllib.request.urlretrieve(img_tag.get('src'), path)
        url = upload(path, str(title) + '.jpg')

        # 坐标
        location_tag = img_tag.find_parent().find_next_sibling('p', class_='contentFont')
        location = location_tag.text.strip() if location_tag else None

        # 窗口位置
        window_tag = location_tag.find_next_sibling('p', class_='contentFont')
        window = window_tag.text.strip() if window_tag else None

        # 小编食评
        comment_tag = window_tag.find_next_sibling('p', class_='contentFont')
        description = comment_tag.text.strip() if comment_tag else None

        # 将这些信息存储为一个字典
        item = {
            'title': title,
            'img_url': url,
            'location': location,
            'window': window,
            'description': description
        }
        # 打印结果
        print(item)
        import_data(item)


url = 'https://m.thepaper.cn/baijiahao_26628231'
save_dir = './images'
download_img(url, save_dir)
