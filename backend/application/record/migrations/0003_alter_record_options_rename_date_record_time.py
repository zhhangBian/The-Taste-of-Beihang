# Generated by Django 4.2.3 on 2024-07-30 16:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("record", "0002_remove_record_dish_name_record_restaurant_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="record",
            options={"verbose_name": "用餐记录", "verbose_name_plural": "用餐记录"},
        ),
        migrations.RenameField(
            model_name="record",
            old_name="date",
            new_name="time",
        ),
    ]
