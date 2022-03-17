from django.db import models

# Create your models here.

#ユーザーモデル
class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    realname = models.CharField(max_length=64, null=True, blank=True)
    py = models.CharField(max_length=64, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    user_regtime = models.DateTimeField(auto_now_add=True)
    user_modtime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    class Meta:
        db_table = 'user'
        verbose_name = 'ユーザー一覧表'
        verbose_name_plural = verbose_name