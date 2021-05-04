# File: tests.py (for backend)
# Author: Danielle Dishop, Colin Seifer
# Description: This file contains the test suite for multiple files and functionalities
#     managed by the backend of Nature's RPG

import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from random import randrange

from .models import Player, Observation
from .serializers import PlayerSerializer

from .Utils.TypeAssign import Type
from .Utils.StatsAssign import FLOOR, CEILING, INCREASE_MOD, DECREASE_MOD, QUALITY_MOD, Stats
from .Utils.Leveling import LEVEL_BREAKPOINTS, CONFIRM_EXP, CalcLevel, ConfirmExpGain
from .Utils.LoadDatabase import LoadDatabase
from .Battle import Moves
from .Battle import LoadObservation
from .Battle import BattleCalc
from .Battle import BattleSys

client = Client()

# Create your tests here.
class PlayerCreationTest(TestCase):
    def setUp(self):
        Player.objects.create(iNat_user_id=1, username="omarm6581")
        Player.objects.create(iNat_user_id=2, username="JulesTheCat")

    def test_player_1(self):
        player_1 = Player.objects.get(iNat_user_id=1)
        self.assertEqual(player_1.iNat_user_id, 1)
        self.assertEqual(player_1.username, "omarm6581")

    def test_player_2(self):
        player_2=Player.objects.get(iNat_user_id=2)
        self.assertEqual(player_2.iNat_user_id, 2)
        self.assertEqual(player_2.username, "JulesTheCat")


class GetAllPlayers(TestCase):
    def setUp(self):
        Player.objects.create(iNat_user_id=1, username="omarm6581")
        Player.objects.create(iNat_user_id=2, username="JulesTheCat")
        Player.objects.create(iNat_user_id=3, username="theverybest")
        Player.objects.create(iNat_user_id=4, username="447isawesome")

    def test_get_all_players(self):
        response = client.get(reverse('players'))
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSinglePlayer(TestCase):
    def setUp(self):
        self.omar = Player.objects.create(iNat_user_id=1, username="omarm6581")
        self.jules = Player.objects.create(iNat_user_id=2, username="JulesTheCat")
        self.best = Player.objects.create(iNat_user_id=3, username="theverybest")
        self.awe = Player.objects.create(iNat_user_id=4, username="447isawesome")

    def test_get_valid_certain_player(self):
        response = client.get(reverse('player', args=[self.best.pk]))
        player = Player.objects.get(iNat_user_id=3)
        serializer = PlayerSerializer(player)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_certain_player(self):
        response = client.get(reverse('player', args=[12]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewPlayer(TestCase):
    def setUp(self):
        self.valid_payload = {
            'iNat_user_id': 1,
            'username': 'omarm6581'
        }
        self.invalid_payload = {
            'iNat_user_id': 'one',
            'username': 'omarm6581'
        }

    def test_create_valid_player(self):
        response = client.post(reverse('players'), data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_player(self):
        response = client.post(reverse('players'), data=json.dumps(self.invalid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdatePlayer(TestCase):
    def setUp(self):
        self.omar = Player.objects.create(iNat_user_id=1, username="omarm6581")
        self.jules = Player.objects.create(iNat_user_id=2, username="JulesTheCat")
        self.best = Player.objects.create(iNat_user_id=3, username="theverybest")
        self.awe = Player.objects.create(iNat_user_id=4, username="447isawesome")

        self.valid_payload = {
            'iNat_user_id': 5,
            'username': 'testing'
        }

        self.invalid_payload = {
            'iNat_user_id': 'one',
            'username': 'testing'
        }

    def test_valid_player_update(self):
        response = client.put(reverse('player', args=[self.omar.pk]), data=json.dumps(self.valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_player_update(self):
        response = client.put(reverse('player', args=[self.omar.pk]), data=json.dumps(self.invalid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeletePlayer(TestCase):
    def setUp(self):
        self.omar = Player.objects.create(iNat_user_id=1, username="omarm6581")
        self.jules = Player.objects.create(iNat_user_id=2, username="JulesTheCat")

    def test_valid_delete_player(self):
        response = client.delete(reverse('player', args=[self.omar.pk]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_player(self):
        response = client.delete(reverse('player', args=[3]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class TypeGenTestCase(TestCase):
    def test_Undefined(self):
        uType = Type(0)
        self.assertEqual(uType.AssignType(), 'Undefined')

    def test_Mammalia(self):
        mType = Type(40151)
        self.assertEqual(mType.AssignType(), 'Mammalia')

    def test_Actinopterygii(self):
        aType = Type(47178)
        self.assertEqual(aType.AssignType(), 'Actinopterygii')

    def test_Fungi(self):
        fType = Type(47170)
        self.assertEqual(fType.AssignType(), 'Fungi')

    def test_Reptilia(self):
        rType = Type(26036)
        self.assertEqual(rType.AssignType(), 'Reptilia')

    def test_Chromista(self):
        cType = Type(48222)
        self.assertEqual(cType.AssignType(), 'Chromista')

    def test_Plantae(self):
        pType = Type(47126)
        self.assertEqual(pType.AssignType(), 'Plantae')

    def test_Animalia(self):
        aType = Type(1)
        self.assertEqual(aType.AssignType(), 'Animalia')

    def test_Mollusca(self):
        moType = Type(47115)
        self.assertEqual(moType.AssignType(), 'Mollusca')

    def test_Insecta(self):
        iType = Type(47158)
        self.assertEqual(iType.AssignType(), 'Insecta')

    def test_Aves(self):
        avType = Type(3)
        self.assertEqual(avType.AssignType(), 'Aves')

    def test_Amphibia(self):
        amType = Type(20978)
        self.assertEqual(amType.AssignType(), 'Amphibia')

    def test_Arachnida(self):
        arType = Type(47119)
        self.assertEqual(arType.AssignType(), 'Arachnida')

    def test_Protozoa(self):
        prType = Type(47686)
        self.assertEqual(prType.AssignType(), 'Protozoa')

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

    # Tests that ConfirmExpGain correctly updates xp and confirmations when it should
    def test_confirm_exp_gain(self):
        # This observation has 2 confirmations when the test is written
        o_id = 13713430
        confirmations = 2

        # Place the observation into the database
        u = Player(iNat_user_id=1, username='test')
        u.save()
        o = Observation(owner=u, obs_id=o_id)
        o.save()

        # Call the function and check that it gained the appropriate amount of xp and levels
        ConfirmExpGain(o_id)
        o = Observation.objects.get(obs_id=o_id)
        self.assertEqual(o.total_xp, CONFIRM_EXP*confirmations)
        self.assertEqual(o.level, 3)  # 1000 EXP is level 3
        self.assertEqual(o.num_of_confirmations, 2)

        # Remove the observation from the database
        Observation.objects.filter(obs_id=o_id).delete()
        Player.objects.filter(iNat_user_id=1).delete()

    # Tests the ConfirmExpGain does not grant xp or change confirmations when it does not need to
    def test_confirm_exp_none(self):
        # This observation has 2 confirmations when the test is written
        o_id = 13713430
        confirmations = 2

        # Place the observation into the database
        u = Player(iNat_user_id=1, username='test')
        u.save()
        o = Observation(owner=u, obs_id=o_id, num_of_confirmations=confirmations)
        o.save()

        # Call the function and check that it gained no xp
        ConfirmExpGain(o_id)
        o = Observation.objects.get(obs_id=o_id)
        self.assertEqual(o.total_xp, 0)
        self.assertEqual(o.level, 1)
        self.assertEqual(o.num_of_confirmations, 2)

        # Remove the observation from the database
        Observation.objects.filter(obs_id=o_id).delete()
        Player.objects.filter(iNat_user_id=1).delete()

    # Tests that ConfirmExpGain does not remove xp or confirmations if an error occurs
    # (i.e. if an observation has more confirmations in the database than on iNaturalist)
    def test_confirm_exp_error(self):
        # This observation has 2 confirmations when the test is written
        o_id = 13713430
        confirmations = 2

        # Place the observation into the database
        u = Player(iNat_user_id=1, username='test')
        u.save()
        o = Observation(owner=u, obs_id=o_id, num_of_confirmations=confirmations+1)
        o.save()

        # Call the function and check that it gained and lost no xp
        ConfirmExpGain(o_id)
        o = Observation.objects.get(obs_id=o_id)
        self.assertEqual(o.total_xp, 0)
        self.assertEqual(o.level, 1)
        self.assertEqual(o.num_of_confirmations, 3)

        # Remove the observation from the database
        Observation.objects.filter(obs_id=o_id).delete()
        Player.objects.filter(iNat_user_id=1).delete()

class TestStats(TestCase):

    # test that moves are imported correctly
    def test_moves(self):
        test_move = Moves.Moves()
        move = test_move.RetMove("Nature's Wrath")
        # test import
        self.assertEqual(move.get("name"), "Nature's Wrath")
        # test that invalid move returns None
        move = test_move.RetMove("invalid_move")
        self.assertIsNone(move)

    # test that observation is created correctly
    def test_observation(self):
        stats = [100, 100, 100, 100, 100, 100]
        moves = ["Nature's Wrath", "Autotomy", "Spine Shield", "Mimesis"]
        obs_type = "Insecta"
        test_obs = LoadObservation.LoadObservation(obs_type, moves, stats)
        # test that values are non-empty
        self.assertEqual(test_obs.stats[0], 100)
        self.assertEqual(test_obs.moves[0].get("name"), "Nature's Wrath")
        self.assertEqual(test_obs.stat_mod[0], 0)
        self.assertEqual(test_obs.observation_type, "Insecta")

    # test that battle calculations are correctly computed
    def test_battleCalc(self):
        hit = 0
        miss = 0
        for i in range(1000):
            res = BattleCalc.Hit(80, 100, 100)
            if(res):
                hit += 1
            else:
                miss += 1
        # test that some moves hit and some missed
        self.assertTrue(hit > 0 and miss > 0)
        # test that damage is calculated correctly
        self.assertEqual(BattleCalc.Damage(100, 100, 80), 80)
        # test that speed is computed correctly
        self.assertTrue(BattleCalc.Speed(100, 0.2, 100, 0) > 0)
        self.assertTrue(BattleCalc.Speed(100, 0, 101, 0) < 0)
        self.assertEqual(BattleCalc.Speed(100, 0.5, 100, 0.5), 0)

    # test that battle system works properly
    def test_battle_sys(self):
        stats = [100, 100, 100, 100, 100, 100]
        moves = ["Nature's Wrath", "Autotomy", "Sacrificial Tail", "Mimesis"]
        obs_type = "Insecta"
        observations = []
        # create list of 6 observations
        for i in range(6):
            observations.append(LoadObservation.LoadObservation(obs_type, moves, stats))
        # create battle object
        test_battle = BattleSys.Battle(observations)
        # test battle object observations size
        self.assertEqual(len(test_battle.observations), 6)
        # test that observations were imported correctly
        self.assertEqual(test_battle.observations[0].stats[0], 100)

        # test get methods in range
        self.assertEqual(test_battle.GetFlavorText(1), "The observation invokes nature’s wrath. Raises all stats by 20%.")
        self.assertEqual(test_battle.GetBP(4), 60)
        self.assertEqual(test_battle.GetACC(4), 100)

        # test get methods out of range
        self.assertIsNone(test_battle.GetFlavorText(5))
        self.assertIsNone(test_battle.GetBP(1))
        self.assertIsNone(test_battle.GetACC(1))
        self.assertIsNone(test_battle.GetBP(5))
        self.assertIsNone(test_battle.GetACC(5))

        # test set methods
        # valid input
        test_battle.SetSwitch(1)
        self.assertEqual(test_battle.switch, 1)
        # test invalid input
        test_battle.SetSwitch(6)
        self.assertEqual(test_battle.switch, 1)
        # valid input
        test_battle.SetMoveChoice(4)
        self.assertEqual(test_battle.move_choice, 4)
        # test invalid input
        test_battle.SetMoveChoice(0)
        self.assertEqual(test_battle.move_choice, 4)
        test_battle.SetSwitch(0)
        # reset values
        test_battle.PlayerTurn()

        # test player turn switch
        test_battle.switch = 1
        test_battle.PlayerTurn()
        self.assertEqual(test_battle.p1_active_obs, 1)
        # test that switch is reset
        self.assertEqual(test_battle.switch, -1)

        #test player turn move
        test_battle.move_choice = 4
        test_battle.PlayerTurn()
        self.assertEqual(test_battle.p1_move, test_battle.observations[1].moves[3])
        # test that move is reset
        self.assertEqual(test_battle.move_choice, 0)

        # test opponent not ai turn switch
        test_battle.switch = 4
        test_battle.OpponentTurn(False)
        self.assertEqual(test_battle.p2_active_obs, 4)
        # test that switch is reset
        self.assertEqual(test_battle.switch, -1)

        #test opponent not ai turn move
        test_battle.move_choice = 4
        test_battle.OpponentTurn(False)
        self.assertEqual(test_battle.p2_move, test_battle.observations[4].moves[3])
        # test that move is reset
        self.assertEqual(test_battle.move_choice, 0)

        # test priority
        # p1_move should have higher priority
        test_battle.p1_move = test_battle.observations[1].moves[2]
        test_battle.p2_move = test_battle.observations[1].moves[3]
        # p1 priority indicated by return of 0
        self.assertEqual(test_battle.Priority(), 0)

        # p2_move should have higher priority
        test_battle.p1_move = test_battle.observations[1].moves[3]
        test_battle.p2_move = test_battle.observations[1].moves[2]
        # p2 priority indicated by return of 1
        self.assertEqual(test_battle.Priority(), 1)

        # test player switch
        test_battle.switch = 2
        test_battle.PlayerSwitch()
        self.assertEqual(test_battle.p1_active_obs, 2)
        # test that switch is reset
        self.assertEqual(test_battle.switch, -1)

        # test opponent not ai switch
        test_battle.switch = 5
        test_battle.OpponentSwitch(False)
        self.assertEqual(test_battle.p2_active_obs, 5)
        # test that switch is reset
        self.assertEqual(test_battle.switch, -1)

        # test attack not ai
        test_battle.p1_move = test_battle.observations[test_battle.p1_active_obs].moves[3]
        test_battle.p2_move = test_battle.observations[test_battle.p2_active_obs].moves[0]
        test_battle.Attack(False)
        # test that p1 attack reduces HP of p2 observation by 60
        self.assertEqual(test_battle.observations[5].stats[0], 40)
        # knock out p2 observation
        test_battle.switch = 4
        test_battle.p1_move = test_battle.observations[test_battle.p1_active_obs].moves[3]
        test_battle.p2_move = test_battle.observations[test_battle.p2_active_obs].moves[0]
        test_battle.Attack(False)
        self.assertTrue(test_battle.observations[5].stats[0] <= 0)
        # test that p2 observation was switched to 4
        self.assertEqual(test_battle.p2_active_obs, 4)
        # knock out p2 observation 4
        test_battle.p1_move = test_battle.observations[test_battle.p1_active_obs].moves[3]
        test_battle.p2_move = test_battle.observations[test_battle.p2_active_obs].moves[0]
        test_battle.Attack(False)
        test_battle.switch = 3
        test_battle.p1_move = test_battle.observations[test_battle.p1_active_obs].moves[3]
        test_battle.p2_move = test_battle.observations[test_battle.p2_active_obs].moves[0]
        test_battle.Attack(False)
        self.assertTrue(test_battle.observations[4].stats[0] <= 0)
        self.assertEqual(test_battle.p2_active_obs, 3)
        # attack one more time to get p2 final observation to 40hp
        test_battle.p1_move = test_battle.observations[test_battle.p1_active_obs].moves[3]
        test_battle.p2_move = test_battle.observations[test_battle.p2_active_obs].moves[0]
        test_battle.Attack(False)

        # test final turn in BattleLoop with ai
        test_battle.move_choice = 4
        # player 1 should win which is returned as a 0
        self.assertEqual(test_battle.BattleLoop(True), 0)

    # test that battle effects work properly
    def test_battle_effects(self):
        stats = [100, 100, 100, 100, 100, 100]
        moves = ["Night Vision", "Avoid Detection", "Play Dead", "Develop Tools"]
        obs_type = "Insecta"
        observations = []
        # create new list of observations
        for i in range(6):
            observations.append(LoadObservation.LoadObservation(obs_type, moves, stats))
        # create battle object
        test_battle = BattleSys.Battle(observations)

        # test next sure hit
        test_battle.p1_active_obs = 0
        test_battle.p2_active_obs = 3
        test_battle.p1_move = test_battle.observations[3].moves[0]
        test_battle.p1_move_prev = test_battle.observations[0].moves[0]
        test_battle.p1_move = test_battle.observations[0].moves[3]
        # placeholder until I get opp_dmg set up
        self.assertTrue(True)

class LoadDatabaseTestCase(TestCase):
    # Test loading a user and their observations
    def test_load_database(self):
        # This user is named neurodoc, and has 2 insect observations at the writing of this test
        u_id = 1042661

        LoadDatabase(1042661)

        # Check that the user and their observations are in the database
        u_results = Player.objects.filter(iNat_user_id=u_id)
        u_count = u_results.count()
        self.assertEqual(u_count, 1)
        if u_count == 1:
            # Test that database loaded correctly
            user = Player.objects.get(iNat_user_id=u_id)
            self.assertEqual(user.username, "neurodoc")

            # Test that the correct number of observations were loaded
            o_count = Observation.objects.filter(owner=user).count()
            self.assertEqual(user.num_of_obs, 2)
            self.assertEqual(o_count, 2)

            # Check that the first observation loaded correctly
            obs_1 = Observation.objects.filter(obs_id=13713430).count()
            self.assertEqual(obs_1, 1)
            if obs_1 == 1:
                obs_1 = Observation.objects.get(obs_id=13713430)
                self.assertEqual(obs_1.owner, user)
                self.assertEqual(obs_1.taxa, "Insecta")
                self.assertEqual(obs_1.total_xp, CONFIRM_EXP*2)
                self.assertEqual(obs_1.level, 3)
                self.assertEqual(obs_1.num_of_confirmations, 2)
                self.assertEqual(obs_1.quality, "research")
                # Observation is research grade insect, check attributes
                self.assertGreaterEqual(obs_1.hp, FLOOR + (QUALITY_MOD*2))
                self.assertLess(obs_1.hp, CEILING)
                self.assertGreaterEqual(obs_1.strength, FLOOR + (QUALITY_MOD*2))
                self.assertLess(obs_1.strength, CEILING)
                self.assertGreaterEqual(obs_1.evasion, FLOOR + (QUALITY_MOD * 2))
                self.assertLess(obs_1.evasion, CEILING)
                self.assertGreaterEqual(obs_1.accuracy, FLOOR + (QUALITY_MOD * 2))
                self.assertLess(obs_1.accuracy, CEILING)
                self.assertGreaterEqual(obs_1.speed, round((FLOOR + (QUALITY_MOD * 2)) * INCREASE_MOD))
                self.assertLess(obs_1.speed, round(CEILING * INCREASE_MOD))
                self.assertGreaterEqual(obs_1.defense, round((FLOOR + (QUALITY_MOD * 2)) * DECREASE_MOD))
                self.assertLess(obs_1.defense, round(CEILING * DECREASE_MOD))

            # Check that the second observation loaded correctly
            obs_2 = Observation.objects.filter(obs_id=13713355).count()
            self.assertEqual(obs_2, 1)
            if obs_2 == 1:
                obs_2 = Observation.objects.get(obs_id=13713355)
                self.assertEqual(obs_2.owner, user)
                self.assertEqual(obs_2.taxa, "Insecta")
                self.assertEqual(obs_2.total_xp, CONFIRM_EXP * 1)
                self.assertEqual(obs_2.level, 2)
                self.assertEqual(obs_2.num_of_confirmations, 1)
                self.assertEqual(obs_2.quality, "needs_id")
                # Observation is needs_id insect, check attributes
                self.assertGreaterEqual(obs_2.hp, FLOOR)
                self.assertLess(obs_2.hp, CEILING)
                self.assertGreaterEqual(obs_2.strength, FLOOR)
                self.assertLess(obs_2.strength, CEILING)
                self.assertGreaterEqual(obs_2.evasion, FLOOR)
                self.assertLess(obs_2.evasion, CEILING)
                self.assertGreaterEqual(obs_2.accuracy, FLOOR)
                self.assertLess(obs_2.accuracy, CEILING)
                self.assertGreaterEqual(obs_2.speed, round(FLOOR * INCREASE_MOD))
                self.assertLess(obs_2.speed, round(CEILING * INCREASE_MOD))
                self.assertGreaterEqual(obs_2.defense, round(FLOOR * DECREASE_MOD))
                self.assertLess(obs_2.defense, round(CEILING * DECREASE_MOD))

            # Clean up the database
            Observation.objects.filter(owner=user).delete()
        else:
            # This is an error of the user, don't need to/can't check observations
            self.assertEqual(1,0)

        # Clean up the database
        Player.objects.filter(iNat_user_id=u_id).delete()

    # Test that LoadDatabase does not load things twice
    def test_load_database_twice(self):
        # This user is named neurodoc, and has 2 insect observations at the writing of this test
        u_id = 1042661

        LoadDatabase(1042661)
        LoadDatabase(1042661)

        # Check that the user and their observations are in the database
        u_results = Player.objects.filter(iNat_user_id=u_id)
        u_count = u_results.count()
        self.assertEqual(u_count, 1)
        if u_count == 1:
            u_results = Player.objects.get(iNat_user_id=u_id)
            o_count = Observation.objects.filter(owner=u_results).count()
            self.assertEqual(o_count, 2)
            Observation.objects.filter(owner=u_results).delete()
        else:
            # This is an error of the user, don't need to/can't check observations
            self.assertEqual(1, 0)

        Player.objects.filter(iNat_user_id=u_id).delete()
