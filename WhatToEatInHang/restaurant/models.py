from django.db import models


class Restaurant(models.Model):
    """
    restaurant model
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    # address = models.ForeignKey('Address', on_delete=models.CASCADE, null=True)
    detail_addr = models.CharField(max_length=200, null=True, blank=True)
    # phone = models.CharField(max_length=20, null=True, blank=True)
    # img = models.ImageField(upload_to='restaurant/', default='restaurant/default.png', verbose_name='店铺图像')
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # creator = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    # tags = models.ManyToManyField('Tag', related_name='restaurants', through='RestaurantTag')


class Dish(models.Model):
    """
    dish model
    """
    dish_name = models.CharField(max_length=20)
    dish_description = models.CharField(max_length=200)
    dish_price = models.FloatField()
    dish_img = models.ImageField(upload_to='dish/', default='dish/default.png', verbose_name='dish picture')


class Post(models.Model):
    """
    posts under restaurants
    """
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=2000)
    grade = models.IntegerField(default=0, choices=((0, '未评分'), (1, '一星'), (2, '二星'), (3, '三星'), (4, '四星'), (5, '五星')))
    avg_price = models.IntegerField(default=0)
    restaurant = models.ForeignKey('Restaurant', related_name='posts', on_delete=models.CASCADE)
    creator = models.ForeignKey('users.User', related_name='posts', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    agrees = models.ManyToManyField('users.User', related_name='agreedPosts')
    # image = models.ImageField(upload_to='post_image/', default='post_image/default.png')
    # recommend_dish = models.ManyToManyField('Dish', related_name='recommended_by', through='RecommendDish')
