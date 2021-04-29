# File: LoadDatabase.py
# Author: Danielle Dishop
# Description: This file contains functionality to take in a user id and load the user data
#     as well as all observations into the database, with the correct type and stat assignments

from pyinaturalist.node_api import get_user_by_id, get_observations

from ..models import User, Observation

from .TypeAssign import Type
from .StatsAssign import Stats
from .Leveling import ConfirmExpGain

def LoadDatabase(u_id):
    # Check if the user is already in the database
    results = User.objects.filter(inat_user_id=u_id)
    name = ""
    if len(results) == 0:
        # request user data from the iNat API and add the user to the database
        user = get_user_by_id(u_id)
        name = user.get('login')
        user = User(inat_user_id=u_id, username=name)
        user.save()

    # If/when logging is implemented, output an error because more than one user in the database
    # is associated with a single id
    elif len(results) > 1:
        return

    else:
        name = results.username

    # Request the user's observations
    observations = get_observations(user_id=u_id)
    observations = observations.get('results')

    for obs in observations:
        # For each observation, check if it is already added to the database
        o_id = obs.get('id')
        results = Observation.objects.filter(obs_id=o_id)

        # If an observation isn't in the database, assign it a type and stats, and add it
        if len(results) == 0:
            taxon = obs.get('taxon')
            o_type_obj = Type(taxon.get('id'), taxon.get('ancestor_ids'))
            o_type = o_type_obj.AssignType()

            stats_obj = Stats(o_type, obs.get('quality_grade'))
            stats = stats_obj.AssignStats()

            new_o = Observation(
                username=name,
                obs_id=o_id,
                hp=stats.get("Health"),
                strength=stats.get("Attack"),
                defense=stats.get("Defense"),
                evasion=stats.get("Evasion"),
                accuracy=stats.get("Accuracy"),
                speed=stats.get("Speed")
            )
            new_o.save()

            # Determine if the new observation gets initial xp based on confirmations
            ConfirmExpGain(o_id)

        # If/when logging is implemented, output an error because more than one observation
        # in the database is associated with a single id
        if len(results) > 1:
            return
