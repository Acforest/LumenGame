# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class Banner(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'banner'


class GameInfo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    url = models.TextField(blank=True, null=True)
    img_url = models.TextField(blank=True, null=True)
    types = models.CharField(max_length=255, blank=True, null=True)
    desc_snippet = models.TextField(blank=True, null=True)
    recent_reviews = models.TextField(blank=True, null=True)
    all_reviews = models.TextField(blank=True, null=True)
    release_date = models.CharField(max_length=255, blank=True, null=True)
    developer = models.TextField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    popular_tags = models.TextField(blank=True, null=True)
    game_details = models.TextField(blank=True, null=True)
    languages = models.TextField(blank=True, null=True)
    achievements = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    game_description = models.TextField(blank=True, null=True)
    mature_content = models.TextField(blank=True, null=True)
    minimum_requirements = models.TextField(blank=True, null=True)
    recommended_requirements = models.TextField(blank=True, null=True)
    original_price = models.CharField(max_length=255, blank=True, null=True)
    discount_price = models.CharField(max_length=255, blank=True, null=True)
    

    class Meta:
        managed = True
        db_table = 'game_info'


class Player(models.Model):
    id = models.BigAutoField(primary_key=True)
    photo = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    qq = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    user = models.OneToOneField(User, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'player'


class Recommend1(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=255)
    preference = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'recommend_1'


class Recommend2(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=255)
    preference = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'recommend_2'


class Repository(models.Model):
    user_id = models.CharField(max_length=255)
    game_name = models.CharField(max_length=255)
    hours = models.FloatField()
    purchase = models.IntegerField()
    play = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'repository'


class GameRank(models.Model):
    rank = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    rank_type = models.CharField(max_length=255, default='hot')
    discount_price = models.CharField(max_length=255, blank=True, null=True)
    discount_pct = models.CharField(max_length=255, blank=True, null=True)
    publish_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rank'