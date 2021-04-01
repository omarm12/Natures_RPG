# File: StatsAssign.py
# Author: Danielle Dishop
# Description: Allows the assignment of stats to an observation based on
#       the type and the quality of the observation

import random

#Constants
FLOOR = 70
CEILING = 130
INCREASE_MOD = 1.25
DECREASE_MOD = 0.75

# List of different stats
STAT_LIST = ["Attack", "Defense", "Health", "Speed", "Evasion", "Accuracy"]

# Dictionary to keep track of which stats are modified for each type
STAT_MOD_DICT = {
    "Mammalia+": "Evasion", "Mammalia-": "Accuracy",
    "Actinopterygii+": "Speed", "Actinopterygii-": "Attack",
    "Fungi+": "Health", "Fungi-": "Evasion",
    "Reptilia+": "Accuracy", "Reptilia-": "Evasion",
    "Chromista+": "Health", "Chromista-": "Speed",
    "Plantae+": "Defense", "Plantae-": "Attack",
    "Mollusca+": "Defense", "Mollusca-": "Speed",
    "Insecta+": "Speed", "Insecta-": "Defense",
    "Aves+": "Accuracy", "Aves-": "Health",
    "Amphibia+": "Attack", "Amphibia-": "Accuracy",
    "Arachnida+": "Attack", "Arachnida-": "Defense",
    "Protozoa+": "Evasion", "Protozoa-": "Health"
}

# Stats class is used to initialize all of the
class Stats:

    def __init__(self, type, quality):
        self.quality = quality
        self.type = type

        # Floor value can be modified by the quality score
        self.floor = FLOOR

    def AssignStats(self):
        stat_dict = {}

        # iterate through the list of stats to assign each
        for stat in STAT_LIST:
            # sets the stat as a random integer between the floor and 130
            stat_dict[stat] = random.randrange(self.floor, CEILING)

            # apply modifier if the stat should be modified
            if STAT_MOD_DICT.get(self.type + "+") == stat:
                stat_dict[stat] = round(stat_dict[stat] * INCREASE_MOD)
            if STAT_MOD_DICT.get(self.type + "-") == stat:
                stat_dict[stat] = round(stat_dict[stat] * DECREASE_MOD)

        # return the complete dictionary of stats
        return stat_dict