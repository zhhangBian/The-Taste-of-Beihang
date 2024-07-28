import os
import re

import django
import requests
from bs4 import BeautifulSoup

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


def find_row_by_value(column_name, value):
    matching_row = df[df[column_name] == value]
    if not matching_row.empty:
        return matching_row.iloc[0]
    else:
        return None


import pandas as pd

df = pd.read_csv("图片链接.csv")


def get_rom_number(value, rol_name):
    for i in range(1, len(df[rol_name])):
        if df[rol_name][i] == value:
            return i
    return 0


def clean_string(text):
    # 正则表达式匹配所有非中文和非英文字符
    pattern = r'[^\u4e00-\u9fffA-Za-z]'
    # 使用re.sub()替换所有匹配的字符为空字符串
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text


def import_data(data):
    dish, created = Dish.objects.update_or_create(
        name=clean_string(data['title']),
        # image=df['image'][get_rom_number(data['title'], 'title')],
        image=data['img_url'],
        address=data['location'],
        price=generate_random_float(8, 18),
        description=data['description'],
        overall_rating=generate_random_real_float(4, 5),
        flavor_rating=generate_random_real_float(4, 5),
        waiting_time=generate_random_float(0, 2),
        restaurant_name=data['window'],
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
        # print(img_tag.get('src'))
        # urllib.request.urlretrieve(img_tag.get('src'), save_dir + '/' + str(title_tag.text) + '.jpg')
        # break
        # print(str(i) + ': ' + str(title_tag.text))
        # i += 1

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
            'title': title_tag.text.strip(),
            'img_url': img_tag['src'],
            'location': location,
            'window': window,
            'description': description
        }
        # 打印结果
        print(item)
        import_data(item)


url = 'https://m.thepaper.cn/baijiahao_26628231'
save_dir = 'images'
download_img(url, save_dir)
