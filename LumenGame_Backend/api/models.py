from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=255, null=False, primary_key=True)
    password = models.CharField(max_length=255, null=False)
    class Meta:
        db_table = 'users'


class Game(models.Model):
    name = models.CharField(max_length=255, null=False)
    # 数据库有问题这里还没写
    class Meta:
        db_table = 'game_info'


class Repository(models.Model):
    user_id = models.CharField(max_length=255, null=False)
    game_name = models.CharField(max_length=255, null=False)
    hours = models.FloatField(null=False)
    purchase = models.SmallIntegerField	(null=False)
    play = models.SmallIntegerField	(null=False)
    class Meta:
        db_table = 'repository'