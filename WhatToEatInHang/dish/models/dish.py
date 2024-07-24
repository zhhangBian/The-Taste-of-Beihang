# 描述了具体的菜品

from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name