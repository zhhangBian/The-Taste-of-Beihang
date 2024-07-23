from django.db import models


class Comment(models.Model):
    """
    comments under dishes
    """
    content = models.CharField(max_length=200)
    comment_time = models.DateTimeField(auto_now_add=True)
    grade = models.IntegerField(default=0, choices=((0, '未评分'), (1, '一星'), (2, '二星'), (3, '三星'), (4, '四星'), (5, '五星')))

    # refer_post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)

    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')

    # 这个是什么？？？
    agrees = models.ManyToManyField('users.User', related_name='agreedComments')

