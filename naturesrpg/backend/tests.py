from django.test import TestCase
from random import randrange

from .TypeAssign import Type
from .StatsAssign import FLOOR, CEILING, INCREASE_MOD, DECREASE_MOD, QUALITY_MOD, Stats
from .Leveling import LEVEL_BREAKPOINTS, CalcLevel

class StatsGenTestCase(TestCase):

    # Tests that stats are correctly assigned for Mammalia
    def test_Mammalia_needs_ID(self):
        # Mammalia has increased evasion and decreased accuracy
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        mammal = Stats('Mammalia', "needs_id")
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
    def test_Actinopterygii_needs_ID(self):
        # Actinopterygii has increased speed and decreased attack
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        fish = Stats('Actinopterygii', "needs_id")
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
    def test_Fungi_needs_ID(self):
        # Fungi has increased health and decreased evasion
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        fungi = Stats('Fungi', "needs_id")
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
    def test_Reptilia_needs_ID(self):
        # Reptilia has increased accuracy and decreased evasion
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        reptile = Stats('Reptilia', "needs_id")
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
    def test_Chromista_needs_ID(self):
        # Chromista has increased health and decreased speed
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        chromist = Stats('Chromista', "needs_id")
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
    def test_Plantae_needs_ID(self):
        # Plantae has increased defense and decreased attack
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        plant = Stats('Plantae', "needs_id")
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
    def test_Animalia_needs_ID(self):
        # Animalia has no increased or decreased stats
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        animal = Stats('Animalia', "needs_id")
        animalStats = animal.AssignStats()
        for stat in animalStats:
            statValue = animalStats.get(stat)
            if (statValue < FLOOR) or (statValue > CEILING):
                flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Mollusca
    def test_Mollusca_needs_ID(self):
        # Mollusca has increased defense and decreased speed
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        mollusc = Stats('Mollusca', "needs_id")
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
    def test_Insecta_needs_ID(self):
        # Insecta has increased speed and decreased defense
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        insect = Stats('Insecta', "needs_id")
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
    def test_Aves_needs_ID(self):
        # Aves has increased accuracy and decreased health
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        bird = Stats('Aves', "needs_id")
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
    def test_Amphibia_needs_ID(self):
        # Amphibia has increased attack and decreased accuracy
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        amphibian = Stats('Amphibia', "needs_id")
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
    def test_Arachnida_needs_ID(self):
        # Arachnida has increased attack and decreased defense
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        arachnid = Stats('Arachnida', "needs_id")
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
    def test_Protozoa_needs_ID(self):
        # Protozoa has increased evasion and decreased health
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        protozoa = Stats('Protozoa', "needs_id")
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

    def test_Undefined_needs_ID(self):
        # Undefined observations have no increased or decreased stats
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        undef = Stats('Undefined', "needs_id")
        undefStats = undef.AssignStats()
        for stat in undefStats:
            statValue = undefStats.get(stat)
            if (statValue < FLOOR) or (statValue > CEILING):
                flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Mammalia
    def test_Mammalia_casual(self):
        # Mammalia has increased evasion and decreased accuracy
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        mammal = Stats('Mammalia', "casual")
        mammalStats = mammal.AssignStats()
        for stat in mammalStats:
            statValue = mammalStats.get(stat)
            if (stat != "Evasion") and (stat != "Accuracy"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Evasion":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Actinopterygii
    def test_Actinopterygii_casual(self):
        # Actinopterygii has increased speed and decreased attack
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        fish = Stats('Actinopterygii', "casual")
        fishStats = fish.AssignStats()
        for stat in fishStats:
            statValue = fishStats.get(stat)
            if (stat != "Speed") and (stat != "Attack"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Speed":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Attack":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Fungi
    def test_Fungi_casual(self):
        # Fungi has increased health and decreased evasion
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        fungi = Stats('Fungi', "casual")
        fungiStats = fungi.AssignStats()
        for stat in fungiStats:
            statValue = fungiStats.get(stat)
            if (stat != "Health") and (stat != "Evasion"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Health":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Evasion":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Reptilia
    def test_Reptilia_casual(self):
        # Reptilia has increased accuracy and decreased evasion
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        reptile = Stats('Reptilia', "casual")
        reptileStats = reptile.AssignStats()
        for stat in reptileStats:
            statValue = reptileStats.get(stat)
            if (stat != "Accuracy") and (stat != "Evasion"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Evasion":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Chromista
    def test_Chromista_casual(self):
        # Chromista has increased health and decreased speed
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        chromist = Stats('Chromista', "casual")
        chromistStats = chromist.AssignStats()
        for stat in chromistStats:
            statValue = chromistStats.get(stat)
            if (stat != "Health") and (stat != "Speed"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Health":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Speed":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Plantae
    def test_Plantae_casual(self):
        # Plantae has increased defense and decreased attack
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        plant = Stats('Plantae', "casual")
        plantStats = plant.AssignStats()
        for stat in plantStats:
            statValue = plantStats.get(stat)
            if (stat != "Defense") and (stat != "Attack"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Defense":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Attack":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Animalia
    def test_Animalia_casual(self):
        # Animalia has no increased or decreased stats
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        animal = Stats('Animalia', "casual")
        animalStats = animal.AssignStats()
        for stat in animalStats:
            statValue = animalStats.get(stat)
            if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Mollusca
    def test_Mollusca_casual(self):
        # Mollusca has increased defense and decreased speed
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        mollusc = Stats('Mollusca', "casual")
        molluscStats = mollusc.AssignStats()
        for stat in molluscStats:
            statValue = molluscStats.get(stat)
            if (stat != "Defense") and (stat != "Speed"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Defense":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Speed":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Insecta
    def test_Insecta_casual(self):
        # Insecta has increased speed and decreased defense
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        insect = Stats('Insecta', "casual")
        insectStats = insect.AssignStats()
        for stat in insectStats:
            statValue = insectStats.get(stat)
            if (stat != "Speed") and (stat != "Defense"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Speed":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Defense":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Aves
    def test_Aves_casual(self):
        # Aves has increased accuracy and decreased health
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        bird = Stats('Aves', "casual")
        birdStats = bird.AssignStats()
        for stat in birdStats:
            statValue = birdStats.get(stat)
            if (stat != "Accuracy") and (stat != "Health"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Health":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Amphibia
    def test_Amphibia_casual(self):
        # Amphibia has increased attack and decreased accuracy
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        amphibian = Stats('Amphibia', "casual")
        amphibianStats = amphibian.AssignStats()
        for stat in amphibianStats:
            statValue = amphibianStats.get(stat)
            if (stat != "Attack") and (stat != "Accuracy"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Attack":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Arachnida
    def test_Arachnida_casual(self):
        # Arachnida has increased attack and decreased defense
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        arachnid = Stats('Arachnida', "casual")
        arachnidStats = arachnid.AssignStats()
        for stat in arachnidStats:
            statValue = arachnidStats.get(stat)
            if (stat != "Attack") and (stat != "Defense"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Attack":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    flag = False
            elif stat == "Defense":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Protozoa
    def test_Protozoa_casual(self):
        # Protozoa has increased evasion and decreased health
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        protozoa = Stats('Protozoa', "casual")
        protozoaStats = protozoa.AssignStats()
        for stat in protozoaStats:
            statValue = protozoaStats.get(stat)
            if (stat != "Evasion") and (stat != "Health"):
                if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                    flag = False
            elif stat == "Evasion":
                if (statValue < round((FLOOR + QUALITY_MOD) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    flag = False
            elif stat == "Health":
                if (statValue < round((FLOOR + QUALITY_MOD) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    flag = False
        self.assertTrue(flag)

    def test_Undefined_casual(self):
        # Undefined observations have no increased or decreased stats
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        undef = Stats('Undefined', "casual")
        undefStats = undef.AssignStats()
        for stat in undefStats:
            statValue = undefStats.get(stat)
            if (statValue < (FLOOR + QUALITY_MOD)) or (statValue > CEILING):
                flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Mammalia
    def test_Mammalia_research(self):
        # Mammalia has increased evasion and decreased accuracy
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        mammal = Stats('Mammalia', "research")
        mammalStats = mammal.AssignStats()
        for stat in mammalStats:
            statValue = mammalStats.get(stat)
            if (stat != "Evasion") and (stat != "Accuracy"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Evasion":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Actinopterygii
    def test_Actinopterygii_research(self):
        # Actinopterygii has increased speed and decreased attack
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        fish = Stats('Actinopterygii', "research")
        fishStats = fish.AssignStats()
        for stat in fishStats:
            statValue = fishStats.get(stat)
            if (stat != "Speed") and (stat != "Attack"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Speed":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Attack":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Fungi
    def test_Fungi_research(self):
        # Fungi has increased health and decreased evasion
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        fungi = Stats('Fungi', "research")
        fungiStats = fungi.AssignStats()
        for stat in fungiStats:
            statValue = fungiStats.get(stat)
            if (stat != "Health") and (stat != "Evasion"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Health":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Evasion":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Reptilia
    def test_Reptilia_research(self):
        # Reptilia has increased accuracy and decreased evasion
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        reptile = Stats('Reptilia', "research")
        reptileStats = reptile.AssignStats()
        for stat in reptileStats:
            statValue = reptileStats.get(stat)
            if (stat != "Accuracy") and (stat != "Evasion"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Evasion":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Chromista
    def test_Chromista_research(self):
        # Chromista has increased health and decreased speed
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        chromist = Stats('Chromista', "research")
        chromistStats = chromist.AssignStats()
        for stat in chromistStats:
            statValue = chromistStats.get(stat)
            if (stat != "Health") and (stat != "Speed"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Health":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Speed":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Plantae
    def test_Plantae_research(self):
        # Plantae has increased defense and decreased attack
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        plant = Stats('Plantae', "research")
        plantStats = plant.AssignStats()
        for stat in plantStats:
            statValue = plantStats.get(stat)
            if (stat != "Defense") and (stat != "Attack"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Defense":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Attack":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Animalia
    def test_Animalia_research(self):
        # Animalia has no increased or decreased stats
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        animal = Stats('Animalia', "research")
        animalStats = animal.AssignStats()
        for stat in animalStats:
            statValue = animalStats.get(stat)
            if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Mollusca
    def test_Mollusca_research(self):
        # Mollusca has increased defense and decreased speed
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        mollusc = Stats('Mollusca', "research")
        molluscStats = mollusc.AssignStats()
        for stat in molluscStats:
            statValue = molluscStats.get(stat)
            if (stat != "Defense") and (stat != "Speed"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Defense":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Speed":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Insecta
    def test_Insecta_research(self):
        # Insecta has increased speed and decreased defense
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        insect = Stats('Insecta', "research")
        insectStats = insect.AssignStats()
        for stat in insectStats:
            statValue = insectStats.get(stat)
            if (stat != "Speed") and (stat != "Defense"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Speed":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Defense":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Aves
    def test_Aves_research(self):
        # Aves has increased accuracy and decreased health
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        bird = Stats('Aves', "research")
        birdStats = bird.AssignStats()
        for stat in birdStats:
            statValue = birdStats.get(stat)
            if (stat != "Accuracy") and (stat != "Health"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Health":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Amphibia
    def test_Amphibia_research(self):
        # Amphibia has increased attack and decreased accuracy
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        amphibian = Stats('Amphibia', "research")
        amphibianStats = amphibian.AssignStats()
        for stat in amphibianStats:
            statValue = amphibianStats.get(stat)
            if (stat != "Attack") and (stat != "Accuracy"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Attack":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    print("+")
                    flag = False
            elif stat == "Accuracy":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    print("-")
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Arachnida
    def test_Arachnida_research(self):
        # Arachnida has increased attack and decreased defense
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        arachnid = Stats('Arachnida', "research")
        arachnidStats = arachnid.AssignStats()
        for stat in arachnidStats:
            statValue = arachnidStats.get(stat)
            if (stat != "Attack") and (stat != "Defense"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Attack":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    flag = False
            elif stat == "Defense":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Protozoa
    def test_Protozoa_research(self):
        # Protozoa has increased evasion and decreased health
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        protozoa = Stats('Protozoa', "research")
        protozoaStats = protozoa.AssignStats()
        for stat in protozoaStats:
            statValue = protozoaStats.get(stat)
            if (stat != "Evasion") and (stat != "Health"):
                if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                    flag = False
            elif stat == "Evasion":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * INCREASE_MOD)) or (statValue > round(CEILING * INCREASE_MOD)):
                    flag = False
            elif stat == "Health":
                if (statValue < round((FLOOR + (2 * QUALITY_MOD)) * DECREASE_MOD)) or (statValue > round(CEILING * DECREASE_MOD)):
                    flag = False
        self.assertTrue(flag)

    def test_Undefined_research(self):
        # Undefined observations have no increased or decreased stats
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        undef = Stats('Undefined', "research")
        undefStats = undef.AssignStats()
        for stat in undefStats:
            statValue = undefStats.get(stat)
            if (statValue < (FLOOR + (2 * QUALITY_MOD))) or (statValue > CEILING):
                flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Mammalia
    def test_Mammalia_invalid_Quality(self):
        # Mammalia has increased evasion and decreased accuracy
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        mammal = Stats('Mammalia', "invalid_Quality")
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
    def test_Actinopterygii_invalid_Quality(self):
        # Actinopterygii has increased speed and decreased attack
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        fish = Stats('Actinopterygii', "invalid_Quality")
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
    def test_Fungi_invalid_Quality(self):
        # Fungi has increased health and decreased evasion
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        fungi = Stats('Fungi', "invalid_Quality")
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
    def test_Reptilia_invalid_Quality(self):
        # Reptilia has increased accuracy and decreased evasion
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        reptile = Stats('Reptilia', "invalid_Quality")
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
    def test_Chromista_invalid_Quality(self):
        # Chromista has increased health and decreased speed
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        chromist = Stats('Chromista', "invalid_Quality")
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
    def test_Plantae_invalid_Quality(self):
        # Plantae has increased defense and decreased attack
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        plant = Stats('Plantae', "invalid_Quality")
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
    def test_Animalia_invalid_Quality(self):
        # Animalia has no increased or decreased stats
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        animal = Stats('Animalia', "invalid_Quality")
        animalStats = animal.AssignStats()
        for stat in animalStats:
            statValue = animalStats.get(stat)
            if (statValue < FLOOR) or (statValue > CEILING):
                flag = False
        self.assertTrue(flag)

    # Tests that stats are correctly assigned for Mollusca
    def test_Mollusca_invalid_Quality(self):
        # Mollusca has increased defense and decreased speed
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        mollusc = Stats('Mollusca', "invalid_Quality")
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
    def test_Insecta_invalid_Quality(self):
        # Insecta has increased speed and decreased defense
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        insect = Stats('Insecta', "invalid_Quality")
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
    def test_Aves_invalid_Quality(self):
        # Aves has increased accuracy and decreased health
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        bird = Stats('Aves', "invalid_Quality")
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
    def test_Amphibia_invalid_Quality(self):
        # Amphibia has increased attack and decreased accuracy
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        amphibian = Stats('Amphibia', "invalid_Quality")
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
    def test_Arachnida_invalid_Quality(self):
        # Arachnida has increased attack and decreased defense
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        arachnid = Stats('Arachnida', "invalid_Quality")
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
    def test_Protozoa_invalid_Quality(self):
        # Protozoa has increased evasion and decreased health
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        protozoa = Stats('Protozoa', "invalid_Quality")
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

    def test_Undefined_invalid_Quality(self):
        # Undefined observations have no increased or decreased stats
        # Uses a flag to ensure all stats are assigned correctly
        flag = True
        undef = Stats('Undefined', "invalid_Quality")
        undefStats = undef.AssignStats()
        for stat in undefStats:
            statValue = undefStats.get(stat)
            if (statValue < FLOOR) or (statValue > CEILING):
                flag = False
        self.assertTrue(flag)

class LevelingTestCase(TestCase):

    # Tests that CalcLevel returns the right level
    def test_calc_level(self):
        # Define an array of random exp values, each corresponding to a different level
        exp = []
        for i in range(1,20):
            exp.append(randrange(LEVEL_BREAKPOINTS.get(i),LEVEL_BREAKPOINTS.get(i+1)))
        exp.append(randrange(LEVEL_BREAKPOINTS.get(20),500000))

        #Check that each Level is correct
        Flag = True
        for i in range(len(exp)):
            level = CalcLevel(exp[i])
            if level != i + 1:
                print(level, " found, ", i + 1, " expected")
                Flag = False

        self.assertTrue(Flag)