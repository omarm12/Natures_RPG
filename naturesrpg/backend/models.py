from django.db import models

# Create your models here.
class Player(models.Model):
    iNat_user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    num_of_obs = models.IntegerField(default=0)
    team = models.JSONField(default=list, null=True)

class Observation(models.Model):
    owner = models.ForeignKey(Player, on_delete=models.CASCADE)
    obs_id = models.IntegerField(default=0)
    name = models.CharField(max_length=50, default="Observation")
    taxa = models.CharField(max_length=20, default="Undefined")
    hp = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    evasion = models.IntegerField(default=0)
    accuracy = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    total_xp = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    num_of_confirmations = models.IntegerField(default=0)
    move_1 = models.CharField(max_length=50, default="Tackle")
    move_2 = models.CharField(max_length=50, blank=True)
    move_3 = models.CharField(max_length=50, blank=True)
    move_4 = models.CharField(max_length=50, blank=True)
    image_link = models.CharField(max_length=100, blank=True)
    quality = models.CharField(max_length=20, default="casual")
    wiki_link = models.CharField(max_length=100, default="https://en.wikipedia.org/wiki/Main_Page")