# Generated by Django 4.2.3 on 2024-07-26 08:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("comment", "0003_remove_comment_dish_name_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={
                "ordering": ["-date"],
                "verbose_name": "评论",
                "verbose_name_plural": "评论",
            },
        ),
        migrations.RemoveField(
            model_name="comment",
            name="dish",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="restaurant",
        ),
        migrations.AlterField(
            model_name="comment",
            name="content",
            field=models.TextField(max_length=200, verbose_name="内容"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="date",
            field=models.DateTimeField(auto_now_add=True, verbose_name="日期"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="flavour",
            field=models.FloatField(default=0, verbose_name="风味"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="grade",
            field=models.IntegerField(
                choices=[
                    (0, "未评分"),
                    (1, "一星"),
                    (2, "二星"),
                    (3, "三星"),
                    (4, "四星"),
                    (5, "五星"),
                ],
                default=0,
                verbose_name="评分",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="price",
            field=models.FloatField(default=0, verbose_name="价格"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="title",
            field=models.CharField(max_length=50, verbose_name="标题"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="waiting_time",
            field=models.FloatField(default=0, verbose_name="等待时间"),
        ),
    ]
