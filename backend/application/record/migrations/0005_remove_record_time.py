# Generated by Django 4.2.3 on 2024-07-30 16:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("record", "0004_alter_record_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="record",
            name="time",
        ),
    ]
