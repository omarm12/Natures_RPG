from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Player(models.Model):
    iNat_user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    num_of_obs = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    team_mems = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(6)])
    profile_pic = models.CharField(max_length=150, default="https://www.pngitem.com/pimgs/m/30-307416_profile-icon-png-image-free-download-searchpng-employee.png")

    def __str__(self):
        return self.username

class Observation(models.Model):
    owner = models.ForeignKey(Player, on_delete=models.CASCADE)
    obs_id = models.IntegerField(default=0)
    name = models.CharField(max_length=50, default="Observation")
    taxa = models.CharField(max_length=20, default="Undefined")
    is_on_team = models.BooleanField(default=False)
    hp = models.IntegerField(default=0)
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    evasion = models.IntegerField(default=0)
    accuracy = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    total_xp = models.IntegerField(default=0)
    level = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    num_of_confirmations = models.IntegerField(default=0)
    move_1 = models.CharField(max_length=50, default="Tackle")
    move_2 = models.CharField(max_length=50, blank=True)
    move_3 = models.CharField(max_length=50, blank=True)
    move_4 = models.CharField(max_length=50, blank=True)
    image_link = models.CharField(max_length=150, default="https://www.pngitem.com/pimgs/m/30-307416_profile-icon-png-image-free-download-searchpng-employee.png")
    quality = models.CharField(max_length=20, default="needs_id")
    wiki_link = models.CharField(max_length=100, default="https://en.wikipedia.org/wiki/Main_Page")

    def __str__(self):
        return self.obs_id
