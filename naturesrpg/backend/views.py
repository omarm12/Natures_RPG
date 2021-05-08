import os, requests, json, sys

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.urls import reverse
from django.shortcuts import render, redirect

from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import PlayerSerializer, ObsSerializer
from .models import Player, Observation

from .forms import LoginForm
from dotenv import load_dotenv

from pyinaturalist.auth import get_access_token

from .Utils.LoadDatabase import LoadDatabase
from .Battle.LoadObservation import LoadObservation
from .Utils.TypeAssign import Type
from .Battle import BattleSys

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                get_access_token(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                    app_id=os.environ.get("INAT_CLIENT_ID"),
                    app_secret=os.environ.get("INAT_CLIENT_SECRET"),
                )

            except requests.HTTPError:
                return render(request, 'backend/no_inat_acc.html')

            test = requests.get("https://api.inaturalist.org/v1/users/autocomplete?q=" + form.cleaned_data['username'])
            request.session['u'] = test.json()['results'][0]['id']
            LoadDatabase(test.json()['results'][0]['id'])
            return redirect('/?u=' + str(test.json()['results'][0]['id']))
    else:
        form = LoginForm()

    return render(request, 'backend/login.html', {'form': form})

def create_updated_battle(request):
    p1_move = None
    p2_move = None
    p1_move_prev = None
    p2_move_prev = None

    try:
        turn = int(request.data.get('turn'))
        p1_active_obs = int(request.data.get('p1_active_obs'))
        p2_active_obs = int(request.data.get('p2_active_obs'))
        move_choice = int(request.data.get('move_choice'))
        switch = int(request.data.get('switch'))

    except TypeError:
        return None

    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'Battle/moves.json')

    f = open(file_path)
    data = json.load(f)

    for i in range(len(data['moves'])):
        if request.data.get('p1_move') == data['moves'][i]['name']:
            p1_move = data['moves'][i]

        if request.data.get('p2_move') == data['moves'][i]['name']:
            p2_move = data['moves'][i]

        if request.data.get('p1_move_prev') == data['moves'][i]['name']:
            p1_move_prev = data['moves'][i]

        if request.data.get('p2_move_prev') == data['moves'][i]['name']:
            p2_move_prev = data['moves'][i]
            

    battle = BattleSys.Battle(
        request.data.get('observations'),
        turn,
        p1_move,
        p2_move,
        p1_active_obs,
        p2_active_obs,
        p1_move_prev,
        p2_move_prev,
        move_choice,
        switch
    )
    f.close()
    return battle


@api_view(['GET'])
def load_obs(request, id):
    try:
        obs = Observation.objects.get(obs_id=id)

    except Observation.DoesNotExist:
        raise NotFound(detail="Error 404, Observation doesn't exist", code=404)

    taxa = obs.taxa

    moves = [
        obs.move_1,
        obs.move_2,
        obs.move_3,
        obs.move_4
    ]

    stats = [
        obs.hp,
        obs.attack,
        obs.defense,
        obs.evasion,
        obs.accuracy,
        obs.speed
    ]

    loaded = LoadObservation(id, taxa, moves, stats)
    loaded.PopulateMoves()

    json_str = json.dumps(loaded.__dict__, indent=4)
    return Response(data=json_str, status=200)


@api_view(['GET'])
def create_battle(request):
    battle = BattleSys.Battle()
    json_str = json.dumps(battle.__dict__, indent=4)
    return Response(data=json_str, status=200)


@api_view(['GET'])
def battle_loop(request):
    battle = create_updated_battle(request)
    if battle is None:
        return Response(status=400)
    check = battle.BattleLoop(ai=True)
    json_str = json.dumps(battle.__dict__, indent=4)
    #gotta be a better way to do this
    return Response(data=check, status=200+check)


@api_view(['GET'])
def get_move_name(request):
    battle = create_updated_battle(request)
    if battle is None:
        return Response(status=400)


@api_view(['GET'])
def get_flavor_text(request, index):
    battle = create_updated_battle(request)
    if battle is None:
        return Response(status=400)
    flavor = battle.GetFlavorText(index)
    json_str = json.dumps(flavor, indent=4)
    return Response(data=json_str, status=200)


@api_view(['GET'])
def get_bp(request, index):
    battle = create_updated_battle(request)
    if battle is None:
        return Response(status=400)
    bp = battle.GetBP(index)
    json_str = json.dumps(bp, indent=4)
    return Response(data=json_str, status=200)


@api_view(['GET'])
def get_acc(request, index):
    battle = create_updated_battle(request)
    if battle is None:
        return Response(status=400)
    acc = battle.GetACC(index)
    json_str = json.dumps(acc, indent=4)
    return Response(data=json_str, status=200)


@api_view(['GET'])
def set_switch(request, index):
    battle = create_updated_battle(request)
    if battle is None:
        return Response(status=400)
    battle.SetSwitch(index)
    return Response(status=200)


@api_view(['PATCH'])
def set_move_choice(request, index):
    battle = create_updated_battle(request)
    if battle is None:
        return Response(status=400)
    battle.SetMoveChoice(index)
    return Response(status=200)


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class ObsList(generics.ListCreateAPIView):
    serializer_class = ObsSerializer

    def get_queryset(self):
        obs = Observation.objects.filter(owner_id=self.kwargs['owner'])
        if not obs:
            raise NotFound(detail="Error 404, Player doesn't exist or has no observations", code=404)

        return obs


class ObsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ObsSerializer
    queryset = Observation.objects.all()

    def get_object(self):
        try:
            obs = Observation.objects.get(obs_id=self.kwargs['obs'])

        except Observation.DoesNotExist:
            raise NotFound(detail="Error 404, Observation doesn't exist", code=404)

        return obs


    def get_queryset(self):
        obs = Observation.objects.filter(owner_id=self.kwargs['owner'])
        if not obs:
            raise NotFound(detail="Error 404, Player doesn't exist or has no observations", code=404)

        return obs