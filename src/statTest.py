# File: statTest.py
# Author: Danielle Dishop
# Description: tests for the Stats class in TypeAssign.py, using the unittest framework

import unittest

from StatsAssign import FLOOR, CEILING, INCREASE_MOD, DECREASE_MOD, Stats

class TestStats(unittest.TestCase):

    # Tests that stats are correctly assigned for Mammalia
    def test_Mammalia_no_Quality(self):
        # Mammalia has increased evasion and decreased accuracy
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        mammal = Stats('Mammalia', 0)
        mammalStats = mammal.AssignStats()
        for stat in mammalStats:
            statValue = mammalStats.get(stat)
            if (stat != "Evasion") and (stat != "Accuracy"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Evasion":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Actinopterygii
    def test_Actinopterygii_no_Quality(self):
        # Actinopterygii has increased speed and decreased attack
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        fish = Stats('Actinopterygii', 0)
        fishStats = fish.AssignStats()
        for stat in fishStats:
            statValue = fishStats.get(stat)
            if (stat != "Speed") and (stat != "Attack"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Speed":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Attack":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Fungi
    def test_Fungi_no_Quality(self):
        # Fungi has increased health and decreased evasion
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        fungi = Stats('Fungi', 0)
        fungiStats = fungi.AssignStats()
        for stat in fungiStats:
            statValue = fungiStats.get(stat)
            if (stat != "Health") and (stat != "Evasion"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Health":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Evasion":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Reptilia
    def test_Reptilia_no_Quality(self):
        # Reptilia has increased accuracy and decreased evasion
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        reptile = Stats('Reptilia', 0)
        reptileStats = reptile.AssignStats()
        for stat in reptileStats:
            statValue = reptileStats.get(stat)
            if (stat != "Accuracy") and (stat != "Evasion"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Evasion":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Chromista
    def test_Chromista_no_Quality(self):
        # Chromista has increased health and decreased speed
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        chromist = Stats('Chromista', 0)
        chromistStats = chromist.AssignStats()
        for stat in chromistStats:
            statValue = chromistStats.get(stat)
            if (stat != "Health") and (stat != "Speed"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Health":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Speed":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Plantae
    def test_Plantae_no_Quality(self):
        # Plantae has increased defense and decreased attack
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        plant = Stats('Plantae', 0)
        plantStats = plant.AssignStats()
        for stat in plantStats:
            statValue = plantStats.get(stat)
            if (stat != "Defense") and (stat != "Attack"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Defense":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Attack":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Animalia
    def test_Animalia_no_Quality(self):
        # Animalia has no increased or decreased stats
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        animal = Stats('Animalia', 0)
        animalStats = animal.AssignStats()
        for stat in animalStats:
            statValue = animalStats.get(stat)
            if (statValue < FLOOR) or (statValue > CEILING):
                flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Mollusca
    def test_Mollusca_no_Quality(self):
        # Mollusca has increased defense and decreased speed
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        mollusc = Stats('Mollusca', 0)
        molluscStats = mollusc.AssignStats()
        for stat in molluscStats:
            statValue = molluscStats.get(stat)
            if (stat != "Defense") and (stat != "Speed"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Defense":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Speed":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Insecta
    def test_Insecta_no_Quality(self):
        # Insecta has increased speed and decreased defense
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        insect = Stats('Insecta', 0)
        insectStats = insect.AssignStats()
        for stat in insectStats:
            statValue = insectStats.get(stat)
            if (stat != "Speed") and (stat != "Defense"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Speed":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Defense":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Aves
    def test_Aves_no_Quality(self):
        # Aves has increased accuracy and decreased health
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        bird = Stats('Aves', 0)
        birdStats = bird.AssignStats()
        for stat in birdStats:
            statValue = birdStats.get(stat)
            if (stat != "Accuracy") and (stat != "Health"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Health":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Amphibia
    def test_Amphibia_no_Quality(self):
        # Amphibia has increased attack and decreased accuracy
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        amphibian = Stats('Amphibia', 0)
        amphibianStats = amphibian.AssignStats()
        for stat in amphibianStats:
            statValue = amphibianStats.get(stat)
            if (stat != "Attack") and (stat != "Accuracy"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Attack":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Arachnida
    def test_Arachnida_no_Quality(self):
        # Arachnida has increased attack and decreased defense
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        arachnid = Stats('Arachnida', 0)
        arachnidStats = arachnid.AssignStats()
        for stat in arachnidStats:
            statValue = arachnidStats.get(stat)
            if (stat != "Attack") and (stat != "Defense"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Attack":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    flag = False
            elif stat == "Defense":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Protozoa
    def test_Protozoa_no_Quality(self):
        # Protozoa has increased evasion and decreased health
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        protozoa = Stats('Protozoa', 0)
        protozoaStats = protozoa.AssignStats()
        for stat in protozoaStats:
            statValue = protozoaStats.get(stat)
            if (stat != "Evasion") and (stat != "Health"):
                if (statValue < FLOOR) or (statValue > CEILING):
                    flag = False
            elif stat == "Evasion":
                if (statValue < round(FLOOR * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    flag = False
            elif stat == "Health":
                if (statValue < round(FLOOR * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    flag = False
        self.assertTrue(flag)

if __name__ == '__main__':
    unittest.main()