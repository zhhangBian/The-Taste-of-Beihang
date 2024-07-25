# 描述了具体的菜品

from django.db import models

from comment.models import Comment


class Dish(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='dish_images')
    address = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    overall_rating = models.FloatField()
    flavor_rating = models.FloatField()
    waiting_time = models.FloatField()
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.name
