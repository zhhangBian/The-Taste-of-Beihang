# Generated by Django 4.2.3 on 2024-07-30 12:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("record", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="record",
            name="dish_name",
        ),
        migrations.AddField(
            model_name="record",
            name="restaurant_name",
            field=models.CharField(default="默认食堂", max_length=200, verbose_name="所属食堂"),
        ),
    ]
