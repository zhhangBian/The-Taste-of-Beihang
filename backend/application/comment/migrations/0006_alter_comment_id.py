# Generated by Django 4.2.3 on 2024-07-28 04:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("comment", "0005_comment_dish_name_comment_restaurant_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="id",
            field=models.AutoField(
                auto_created=True,
                editable=False,
                primary_key=True,
                serialize=False,
                verbose_name="评论ID",
            ),
        ),
    ]
