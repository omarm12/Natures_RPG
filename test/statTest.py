# File: statTest.py
# Author: Danielle Dishop
# Description: tests for the Stats class in TypeAssign.py, using the unittest framework

import unittest

from src.StatsAssign import FLOOR, CEILING, INCREASE_MOD, DECREASE_MOD, Stats

class TestStats(unittest.TestCase):

    # Tests that stats are correctly assigned for Mammalia
    def test_Mammalia_no_Quality(self):
        # Mammalia has increased evasion and decreased accuracy
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        mammal = Stats('Mammalia', 0)
        mammalStats = mammal.AssignStats()
        for stat in mammalStats:
            if (stat != "Evasion") and (stat != "Accuracy"):
                if (stat < FLOOR) or (stat > CEILING):
                    flag = False
            elif stat == "Evasion":
                if (stat < FLOOR * INCREASE_MOD) or (stat > CEILING * INCREASE_MOD):
                    flag = False
            elif stat == "Accuracy":
                if (stat < FLOOR * DECREASE_MOD) or (stat > CEILING * DECREASE_MOD):
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
            if (stat != "Speed") and (stat != "Attack"):
                if (stat < FLOOR) or (stat > CEILING):
                    flag = False
            elif stat == "Speed":
                if (stat < FLOOR * INCREASE_MOD) or (stat > CEILING * INCREASE_MOD):
                    flag = False
            elif stat == "Attack":
                if (stat < FLOOR * DECREASE_MOD) or (stat > CEILING * DECREASE_MOD):
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
            if (stat != "Health") and (stat != "Evasion"):
                if (stat < FLOOR) or (stat > CEILING):
                    flag = False
            elif stat == "Health":
                if (stat < FLOOR * INCREASE_MOD) or (stat > CEILING * INCREASE_MOD):
                    flag = False
            elif stat == "Evasion":
                if (stat < FLOOR * DECREASE_MOD) or (stat > CEILING * DECREASE_MOD):
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
            if (stat != "Evasion") and (stat != "Accuracy"):
                if (stat < FLOOR) or (stat > CEILING):
                    flag = False
            elif stat == "Accuracy":
                if (stat < FLOOR * INCREASE_MOD) or (stat > CEILING * INCREASE_MOD):
                    flag = False
            elif stat == "Evasion":
                if (stat < FLOOR * DECREASE_MOD) or (stat > CEILING * DECREASE_MOD):
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
            if (stat != "Health") and (stat != "Speed"):
                if (stat < FLOOR) or (stat > CEILING):
                    flag = False
            elif stat == "Health":
                if (stat < FLOOR * INCREASE_MOD) or (stat > CEILING * INCREASE_MOD):
                    flag = False
            elif stat == "Speed":
                if (stat < FLOOR * DECREASE_MOD) or (stat > CEILING * DECREASE_MOD):
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
            if (stat != "Defense") and (stat != "Attack"):
                if (stat < FLOOR) or (stat > CEILING):
                    flag = False
            elif stat == "Defense":
                if (stat < FLOOR * INCREASE_MOD) or (stat > CEILING * INCREASE_MOD):
                    flag = False
            elif stat == "Attack":
                if (stat < FLOOR * DECREASE_MOD) or (stat > CEILING * DECREASE_MOD):
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
            if (stat < FLOOR) or (stat > CEILING):
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
            if (stat != "Defense") and (stat != "Speed"):
                if (stat < FLOOR) or (stat > CEILING):
                    flag = False
            elif stat == "Defense":
                if (stat < FLOOR * INCREASE_MOD) or (stat > CEILING * INCREASE_MOD):
                    flag = False
            elif stat == "Speed":
                if (stat < FLOOR * DECREASE_MOD) or (stat > CEILING * DECREASE_MOD):
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
            if (stat != "Speed") and (stat != "Defense"):
                if (stat < FLOOR) or (stat > CEILING):
                    flag = False
            elif stat == "Speed":
                if (stat < FLOOR * INCREASE_MOD) or (stat > CEILING * INCREASE_MOD):
                    flag = False
            elif stat == "Defense":
                if (stat < FLOOR * DECREASE_MOD) or (stat > CEILING * DECREASE_MOD):
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
            if (stat != "Accuracy") and (stat != "Health"):
                if (stat < FLOOR) or (stat > CEILING):
                    flag = False
            elif stat == "Accuracy":
                if (stat < FLOOR * INCREASE_MOD) or (stat > CEILING * INCREASE_MOD):
                    flag = False
            elif stat == "Health":
                if (stat < FLOOR * DECREASE_MOD) or (stat > CEILING * DECREASE_MOD):
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
            if (stat != "Attack") and (stat != "Accuracy"):
                if (stat < FLOOR) or (stat > CEILING):
                    flag = False
            elif stat == "Attack":
                if (stat < FLOOR * INCREASE_MOD) or (stat > CEILING * INCREASE_MOD):
                    flag = False
            elif stat == "Accuracy":
                if (stat < FLOOR * DECREASE_MOD) or (stat > CEILING * DECREASE_MOD):
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
            if (stat != "Attack") and (stat != "Defense"):
                if (stat < FLOOR) or (stat > CEILING):
                    flag = False
            elif stat == "Attack":
                if (stat < FLOOR * INCREASE_MOD) or (stat > CEILING * INCREASE_MOD):
                    flag = False
            elif stat == "Defense":
                if (stat < FLOOR * DECREASE_MOD) or (stat > CEILING * DECREASE_MOD):
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
            if (stat != "Evasion") and (stat != "Health"):
                if (stat < FLOOR) or (stat > CEILING):
                    flag = False
            elif stat == "Evasion":
                if (stat < FLOOR * INCREASE_MOD) or (stat > CEILING * INCREASE_MOD):
                    flag = False
            elif stat == "Health":
                if (stat < FLOOR * DECREASE_MOD) or (stat > CEILING * DECREASE_MOD):
                    flag = False
        self.assertTrue(flag)

if __name__ == '__main__':
    unittest.main()