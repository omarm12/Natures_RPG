from django.db import models

# Create your models here.
class User(models.Model):
    inat_user_id = models.IntegerField()
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Observation(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    obs_id = models.IntegerField()
    hp = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    evasion = models.IntegerField(default=0)
    accuracy = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    total_xp = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    num_of_confirmations = models.IntegerField(default=0)

    def __str__(self):
        return self.obs_id