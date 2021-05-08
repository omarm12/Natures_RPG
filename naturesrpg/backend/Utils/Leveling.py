# File: Leveling.py
# Author: Danielle Dishop
# Description: This file contains code to implement and track experience points for observations, as well as update them

from pyinaturalist.node_api import get_observations
from ..models import Observation

# Level breakpoints based on Dungeons and Dragons, 5th Edition
LEVEL_BREAKPOINTS = {
    1:0,
    2:300,
    3:900,
    4:2700,
    5:6500,
    6:14000,
    7:23000,
    8:34000,
    9:48000,
    10:64000,
    11:85000,
    12:100000,
    13:120000,
    14:140000,
    15:165000,
    16:195000,
    17:225000,
    18:265000,
    19:305000,
    20:355000
}
CONFIRM_EXP = 500
BATTLE_EXP_WIN = 200
BATTLE_EXP_SHARED_WIN = 50
BATTLE_EXP_LOSE = 50

# The function is passed an amount of experience, and returns the corresponding level of the observation
def CalcLevel(exp):
    # Searches through the level breakpoints, finding the highest level for which the experience breakpoint
    # is less than the passed number
    o_level = 0
    for level in LEVEL_BREAKPOINTS:
        if ((level > o_level) and (exp >= LEVEL_BREAKPOINTS.get(level))):
            o_level = level

    return o_level

# This function is passed an observation id, and updates its experience value in the database if it has
# been confirmed since it was last checked
def ConfirmExpGain(o_id):
    # Query the iNaturalist API and get the number of confirmations
    response = get_observations(id=o_id)
    results = response.get('results')

    # Make sure only one observation is returned
    if len(results) != 1:
        # If/when we implement logging, output an error message
        totalConf = 0
    else:
        obs = results[0]
        totalConf = obs.get('num_identification_agreements')

    # Get the experience and number of previous confirmations from the database
    if Observation.objects.filter(obs_id=o_id).count() == 1:
        observation = Observation.objects.get(obs_id=o_id)
        xp = observation.total_xp
        prevConf = observation.num_of_confirmations

        # Calculate the difference in confirmations and update xp accordingly, then send both numbers to
        # the database
        newConf = totalConf - prevConf
        if (newConf >= 0):
            xp = xp + (newConf * CONFIRM_EXP)

            Observation.objects.filter(obs_id=o_id).update(total_xp=xp, num_of_confirmations=totalConf)
        else:
            # If/when we implement logging, output an error message here
            xp = xp

        # Update the observation's level
        o_level = CalcLevel(xp)
        Observation.objects.filter(obs_id=o_id).update(level=o_level)

# This function is passed a boolean for if the player won or not, and the list of observations from the battle
# It updates the player's observations' xp in the database
def BattleExpGain(winner, active, obs):
    # If the player won, give the active observation 200 xp, and the inactive observations 50
    if (winner == True and len(obs) == 6):
        active_id = active.obs_id
        o = Observation.objects.get(obs_id=active_id)
        xp = o.total_xp
        Observation.objects.filter(obs_id=active_id).update(total_xp=xp+BATTLE_EXP_WIN)

        # The player's other observations are in the first three indices of obs.
        # Check that the active obs isn't added twice
        for i in range(3):
            if obs[i].obs_id != active_id:
                o = Observation.objects.get(obs_id=obs[i].obs_id)
                xp = o.total_xp
                Observation.objects.filter(obs_id=obs[i].obs_id).update(total_xp=xp+BATTLE_EXP_SHARED_WIN)

    # If the player did not win, give the active observation 50 xp
    elif (winner == False and len(obs) == 6):
        active_id = active.obs_id
        o = Observation.objects.get(obs_id=active_id)
        xp = o.total_xp
        Observation.objects.filter(obs_id=active_id).update(total_xp=xp+BATTLE_EXP_LOSE)

    # If either statement didn't fire, there are likely not 6 observations loaded. just return
    # If we had logging implemented, this is where we'd have an error statement
    else:
        return