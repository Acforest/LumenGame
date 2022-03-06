from statistics import mode
from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.URLField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    qq = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'player'

    def __str__(self):
        return str(self.user)


class Game(models.Model):
    name = models.CharField(max_length=255, null=False)
    # 数据库有问题这里还没写
    class Meta:
        db_table = 'game_info'


class Banner(models.Model):
    url = models.URLField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    comment = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'banner'

    def __str__(self):
        return str(self.title)


class Repository(models.Model):
    user_id = models.CharField(max_length=255, null=False)
    game_name = models.CharField(max_length=255, null=False)
    hours = models.FloatField(null=False)
    purchase = models.SmallIntegerField	(null=False)
    play = models.SmallIntegerField	(null=False)
    class Meta:
        db_table = 'repository'