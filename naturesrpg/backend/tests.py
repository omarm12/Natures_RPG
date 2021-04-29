import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from .models import Player
from .serializers import PlayerSerializer

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