# File: Leveling.py
# Author: Danielle Dishop
# Description: This file contains code to implement and track experience points for observations, as well as update them

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

# The function is passed an amount of experience, and returns the corresponding level of the observation
def CalcLevel(exp):
    # Searches through the level breakpoints, finding the highest level for which the experience breakpoint
    # is less than the passed number
    o_level = 0
    for level in LEVEL_BREAKPOINTS:
        if ((level > o_level) and (exp > LEVEL_BREAKPOINTS.get(level))):
            o_level = level

    return o_level 