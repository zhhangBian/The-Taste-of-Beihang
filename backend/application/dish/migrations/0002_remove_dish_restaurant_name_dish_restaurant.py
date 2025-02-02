# Generated by Django 5.0.7 on 2024-07-26 02:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dish", "0001_initial"),
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dish",
            name="restaurant_name",
        ),
        migrations.AddField(
            model_name="dish",
            name="restaurant",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="restaurant.restaurant",
            ),
        ),
    ]
