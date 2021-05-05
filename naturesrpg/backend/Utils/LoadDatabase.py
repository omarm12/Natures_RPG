# File: LoadDatabase.py
# Author: Danielle Dishop
# Description: This file contains functionality to take in a user id and load the user data
#     as well as all observations into the database, with the correct type and stat assignments
import json
from pyinaturalist.node_api import get_user_by_id, get_observations

from ..models import Player, Observation

from .TypeAssign import Type
from .StatsAssign import Stats
from .Leveling import ConfirmExpGain

def LoadDatabase(u_id):
    # Check if the user is already in the database
    results = Player.objects.filter(iNat_user_id=u_id)
    user = ""
    if len(results) == 0:
        # request user data from the iNat API and add the user to the database
        user = get_user_by_id(u_id)
        name = user.get('login')
        icon = user.get('icon_url')
        user = Player(iNat_user_id=u_id, username=name, profile_pic=icon)
        user.save()

    # If/when logging is implemented, output an error because more than one user in the database
    # is associated with a single id

    else:
        user = Player.objects.get(iNat_user_id=u_id)

    # Request the user's observations
    observations = get_observations(user_id=u_id)
    observations = observations.get('results')
    obs_num = len(observations)
    
    if obs_num > user.num_of_obs:
        user.num_of_obs = obs_num
        user.save()

    for obs in observations:
        # For each observation, check if it is already added to the database
        o_id = obs.get('id')
        results = Observation.objects.filter(owner=user, obs_id=o_id)

        # If an observation isn't in the database, assign it a type and stats, and add it
        if len(results) == 0:

            # Update the user's number of observations
            user = Player.objects.get(iNat_user_id=u_id)
            o_num = user.num_of_obs
            Player.objects.filter(iNat_user_id=u_id).update(num_of_obs=o_num+1)

            taxon = obs.get('taxon')
            o_type_obj = Type(taxon.get('id'), taxon.get('ancestor_ids'))
            o_type = o_type_obj.AssignType()

            obs_name = taxon.get('preferred_common_name')
            num_of_confirms = obs.get('num_identification_agreements')

            wiki = taxon.get('wikipedia_url')
            photos = taxon.get('default_photo')
            obs_img = photos.get('url')

            stats_obj = Stats(o_type, obs.get('quality_grade'))
            stats = stats_obj.AssignStats()

            new_o = Observation(
                owner=user,
                obs_id=o_id,
                name=obs_name,
                taxa=o_type,
                hp=stats.get("Health"),
                attack=stats.get("Attack"),
                defense=stats.get("Defense"),
                evasion=stats.get("Evasion"),
                accuracy=stats.get("Accuracy"),
                speed=stats.get("Speed"),
                image_link=obs_img,
                wiki_link=wiki,
                quality=obs.get('quality_grade')
            )
            new_o.save()

            # Determine if the new observation gets initial xp based on confirmations
            ConfirmExpGain(o_id)

        # If/when logging is implemented, output an error because more than one observation
        # in the database is associated with a single id
        if len(results) > 1:
            return
