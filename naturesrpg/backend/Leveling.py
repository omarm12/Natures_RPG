# File: Leveling.py
# Author: Danielle Dishop
# Description: This file contains code to implement and track experience points for observations, as well as update them

from .models import Observation

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
CONFRIM_EXP = 500

# The function is passed an amount of experience, and returns the corresponding level of the observation
def CalcLevel(exp):
    # Searches through the level breakpoints, finding the highest level for which the experience breakpoint
    # is less than the passed number
    o_level = 0
    for level in LEVEL_BREAKPOINTS:
        if ((level > o_level) and (exp > LEVEL_BREAKPOINTS.get(level))):
            o_level = level

    return o_level

# This function is passed an observation id, and updates its experience value in the database if it has
# been confirmed since it was last checked
def ConfirmExpGain(o_id):
    # Query the iNaturalist API and get the number of confirmations
    # Dummy value for now
    totalConf = 10

    # Get the experience and number of previous confirmations from the database
    observation = Observation.objects.get(obs_id=o_id)
    xp = observation.total_xp
    prevConf = observation.num_of_confirmations

    # Calculate the difference in confirmations and update xp accordingly, then send both numbers to
    # the database
    newConf = totalConf - prevConf
    if (newConf >= 0):
        xp = xp + (newConf * CONFRIM_EXP)

        observation.xp = xp
        observation.num_of_confirmations = totalConf
        observation.save()
    else:
        # If/when we implement logging, output an error message here
        xp = xp
