from rest_framework import serializers
from .models import Player, Observation

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['iNat_user_id', 'username', 'num_of_obs', 'team_mems', 'profile_pic']

class ObsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = [ 
            'owner',
            'obs_id',
            'name',
            'taxa',
            'is_on_team',
            'hp', 
            'attack', 
            'defense', 
            'evasion', 
            'accuracy', 
            'speed', 
            'total_xp', 
            'level', 
            'num_of_confirmations',
            'move_1',
            'move_2',
            'move_3',
            'move_4',
            'image_link',
            'quality',
            'wiki_link'
         ]