from django.db import models
from django.contrib.auth.models import User
from django import forms


# Create your models here.

class ConsumerUser(models.Model):

    consumer_user = models.OneToOneField(User)
    consumer_is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.consumer_user.username


class Player(models.Model):
    player_first_name = models.CharField(max_length=40)
    player_last_name = models.CharField(max_length=40)
    player_id = models.IntegerField(auto_created=True)
    player_age = models.IntegerField(max_length=None)

    player_country_choices = (
        ('IND','IND'),
        ('SA','SA'),
        ('AUS','AUS'),
        ('ENG','ENG'),
        ('WI','WI'),
        ('NZ','NZ'),
        ('PAK','PAK'),
        ('SL','SL'),
        ('BAN','BAN'),
    )

    player_country = models.CharField(max_length=10, choices=player_country_choices)

    player_type_choices = (
        ('BAT','BAT'),
        ('BOWL','BOWL'),
        ('WK','WK'),
        ('ALL','ALL'),
    )

    player_type = models.CharField(max_length=10,choices=player_type_choices)
    player_price = models.IntegerField(max_length=None)
    player_image = models.FileField(null=True)

    def __str__(self):
        return self.player_last_name

class PlayerScore(models.Model):
    player_score_belonging_to = models.ForeignKey(Player)
    player_score = models.IntegerField(max_length=None)
    player_is_powerplayer = models.BooleanField(default=False)

    def __str__(self):
        return self.player.player_last_name
