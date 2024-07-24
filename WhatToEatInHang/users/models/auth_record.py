# 记录了当前系统中登录的用户

from django.db import models
from django.contrib.auth import get_user_model


class AuthRecord(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    login_at = models.DateTimeField()
    expires_by = models.DateTimeField()

    class Meta:
        # no permissions needed
        default_permissions = ()

