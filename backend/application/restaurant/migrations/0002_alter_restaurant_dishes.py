# Generated by Django 4.2.3 on 2024-07-26 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("dish", "0003_alter_dish_options_remove_dish_restaurant_and_more"),
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restaurant",
            name="dishes",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="restaurant_dishes",
                to="dish.dish",
            ),
        ),
    ]
