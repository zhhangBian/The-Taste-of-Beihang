# Generated by Django 5.0.7 on 2024-07-26 02:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("comment", "0001_initial"),
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="restaurant",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="restaurant.restaurant",
            ),
        ),
    ]
