# Generated by Django 4.2.3 on 2024-07-30 07:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0012_remove_user_word"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="name",
            field=models.EmailField(
                blank=True, default="默认昵称", max_length=254, verbose_name="昵称"
            ),
        ),
    ]
