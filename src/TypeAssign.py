# file: TypeAssign.py
# author: colin seifer, Danielle Dishop
# description: assigns type and stat modifiers

import random

#Constants
FLOOR = 70
CEILING = 130
INCREASE_MOD = 1.25
DECREASE_MOD = 0.75

# create static dict to keep track of taxa
# keys correspond to iNat taxon ID
TAXA_DICT = {
    47158: 'Insecta',
    26036: 'Reptilia',
    48222: 'Chromista',
    47178: 'Actinopterygii',
    40151: 'Mammalia',
    47170: 'Fungi',
    20978: 'Amphibia',
    47119: 'Arachnida',
    3: 'Aves',
    1: 'Animalia',
    47115: 'Mollusca',
    47126: 'Plantae',
    47686: 'Protozoa'
}

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

# sort by taxon ID and ancestor IDs
class Type:

    # initialize object with taxa ID list
    def __init__(self, taxon_id, ancestor_ids = []):
        self.ancestor_ids = []
        self.ancestor_ids.append(taxon_id)
        self.ancestor_ids.extend(ancestor_ids)

    # assign type
    def AssignType(self):
        # check taxa list for match with taxa dict
        for id in self.ancestor_ids:
            if(TAXA_DICT.get(id) != None):
                return TAXA_DICT.get(id)

        # otherwise, return -1 for error
        return -1


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