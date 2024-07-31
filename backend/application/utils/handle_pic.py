import csv
import os

import requests

from application.utils.pic_upload import upload


# 下载图片的函数
def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        return save_path
    else:
        print(f"Failed to download image from {url}")
        return None


# 删除图片的函数
def delete_image(image_path):
    if os.path.exists(image_path):
        os.remove(image_path)
        print(f"Deleted image {image_path}")
    else:
        print(f"Image {image_path} not found")


# 读取CSV文件并处理图片
with open("data/rubbish_data.csv", "r", encoding='utf-8') as data_file:
    data = list(csv.DictReader(data_file))
    fieldnames = data[0].keys()

    for row in data:
        image_url = row['image']
        image_filename = image_url.split('/')[-1]
        image_path = os.path.join('data', image_filename)  # 替换为你的保存路径

        # 下载图片
        downloaded_image_path = download_image(image_url, image_path)
        if downloaded_image_path:
            # 处理图片
            url = upload(downloaded_image_path, image_filename)
            row['image'] = url
            delete_image(downloaded_image_path)

with open("data/handle_data.csv", "w", encoding='utf-8', newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
