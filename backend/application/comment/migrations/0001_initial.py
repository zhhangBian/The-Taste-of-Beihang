# Generated by Django 5.0.7 on 2024-07-26 02:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("content", models.CharField(max_length=200)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "image",
                    models.CharField(
                        default="https://pigkiller-011955-1319328397.cos.ap-beijing.myqcloud.com/img/202407241935479.jpg",
                        max_length=500,
                        verbose_name="图片",
                    ),
                ),
                (
                    "grade",
                    models.IntegerField(
                        choices=[
                            (0, "未评分"),
                            (1, "一星"),
                            (2, "二星"),
                            (3, "三星"),
                            (4, "四星"),
                            (5, "五星"),
                        ],
                        default=0,
                    ),
                ),
                ("price", models.FloatField(default=0)),
                ("flavour", models.FloatField(default=0)),
                ("waiting_time", models.FloatField(default=0)),
                ("author_id", models.IntegerField(default=0)),
                ("dish_name", models.CharField(max_length=100)),
                ("restaurant_name", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "comments",
                "ordering": ["-date"],
            },
        ),
    ]
