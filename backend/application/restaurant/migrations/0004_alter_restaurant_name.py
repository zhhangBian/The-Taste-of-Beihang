# Generated by Django 4.2.3 on 2024-07-30 19:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0003_remove_restaurant_dishes_restaurant_dishes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restaurant",
            name="name",
            field=models.CharField(
                choices=[
                    ("学一食堂", "学一食堂"),
                    ("学二食堂", "学二食堂"),
                    ("学三食堂", "学三食堂"),
                    ("学四食堂", "学四食堂"),
                    ("学五食堂", "学五食堂"),
                    ("学六食堂", "学六食堂"),
                    ("教工食堂", "教工食堂"),
                    ("清真食堂", "清真食堂"),
                    ("合一厅", "合一厅"),
                    ("东区第一食堂", "东区第一食堂"),
                    ("鼓瑟轩", "鼓瑟轩"),
                    ("西区清真食堂", "西区清真食堂"),
                    ("西区第一食堂", "西区第一食堂"),
                    ("西区第二食堂", "西区第二食堂"),
                    ("西区第三食堂", "西区第三食堂"),
                    ("美食苑", "美食苑"),
                    ("其他", "其他"),
                ],
                default=0,
                max_length=20,
                verbose_name="用餐地点",
            ),
        ),
    ]
