# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class GameInfo(models.Model):
    name = models.CharField(max_length=255)
    url = models.TextField(blank=True, null=True)
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
        managed = False
        db_table = 'game_info'


class Recommend1(models.Model):
    user_id = models.CharField(primary_key=True, max_length=255)
    game1 = models.CharField(max_length=255)
    game2 = models.CharField(max_length=255)
    game3 = models.CharField(max_length=255)
    game4 = models.CharField(max_length=255)
    game5 = models.CharField(max_length=255)
    game6 = models.CharField(max_length=255)
    game7 = models.CharField(max_length=255)
    game8 = models.CharField(max_length=255)
    game9 = models.CharField(max_length=255)
    game10 = models.CharField(max_length=255)
    game11 = models.CharField(max_length=255)
    game12 = models.CharField(max_length=255)
    game13 = models.CharField(max_length=255)
    game14 = models.CharField(max_length=255)
    game15 = models.CharField(max_length=255)
    game16 = models.CharField(max_length=255)
    game17 = models.CharField(max_length=255)
    game18 = models.CharField(max_length=255)
    game19 = models.CharField(max_length=255)
    game20 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'recommend1'


class Recommend2(models.Model):
    user_id = models.CharField(primary_key=True, max_length=255)
    game1 = models.CharField(max_length=255)
    game2 = models.CharField(max_length=255)
    game3 = models.CharField(max_length=255)
    game4 = models.CharField(max_length=255)
    game5 = models.CharField(max_length=255)
    game6 = models.CharField(max_length=255)
    game7 = models.CharField(max_length=255)
    game8 = models.CharField(max_length=255)
    game9 = models.CharField(max_length=255)
    game10 = models.CharField(max_length=255)
    game11 = models.CharField(max_length=255)
    game12 = models.CharField(max_length=255)
    game13 = models.CharField(max_length=255)
    game14 = models.CharField(max_length=255)
    game15 = models.CharField(max_length=255)
    game16 = models.CharField(max_length=255)
    game17 = models.CharField(max_length=255)
    game18 = models.CharField(max_length=255)
    game19 = models.CharField(max_length=255)
    game20 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'recommend2'


class Reposity(models.Model):
    user_id = models.CharField(max_length=255)
    game_name = models.CharField(max_length=255)
    hours = models.FloatField()
    purchase = models.IntegerField()
    play = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reposity'