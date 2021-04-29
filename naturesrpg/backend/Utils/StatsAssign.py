# File: StatsAssign.py
# Author: Danielle Dishop
# Description: Allows the assignment of stats to an observation based on
#       the type and the quality of the observation

from random import randrange

#Constants
FLOOR = 70
CEILING = 130
INCREASE_MOD = 1.25
DECREASE_MOD = 0.75
QUALITY_MOD = 15

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

QUALITY_TAGS = ["needs_id", "casual", "research"]

# Stats class is used to initialize all of the
class Stats:

    def __init__(self, type, quality):
        self.quality = quality
        self.type = type

        # Floor value can be modified by the quality score
        # If the quality is "needs_id", keep the floor as it should be
        if (quality == QUALITY_TAGS[0]):
            self.floor = FLOOR
        # If the quality is "casual", increase the floor by one mod
        elif (quality == QUALITY_TAGS[1]):
            self.floor = FLOOR + QUALITY_MOD
        # If the quality is "research", increase the floor by two mods
        elif (quality == QUALITY_TAGS[2]):
            self.floor = FLOOR + (2 * QUALITY_MOD)
        # Otherise, keep the original floor so it doesn't crash (should also output to logs if/when we set them up)
        else:
            self.floor = FLOOR

    def AssignStats(self):
        stat_dict = {}

        # iterate through the list of stats to assign each
        for stat in STAT_LIST:
            # apply modifier if the stat should be modified
            if STAT_MOD_DICT.get(self.type + "+") == stat:
                stat_dict[stat] = randrange(round(self.floor * INCREASE_MOD), round(CEILING * INCREASE_MOD))
            elif STAT_MOD_DICT.get(self.type + "-") == stat:
                stat_dict[stat] = randrange(round(self.floor * DECREASE_MOD), round(CEILING * DECREASE_MOD))
            else:
                stat_dict[stat] = randrange(self.floor, CEILING)

        # return the complete dictionary of stats
        return stat_dict