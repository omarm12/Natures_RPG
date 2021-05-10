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


def recreate_battle(request):
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


    obs_objs = create_obs(request)
    battle = BattleSys.Battle(
        obs_objs,
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


def create_obs(request):
    obs = eval(request.data.get('observations'))
    obs_objs = []
    for i in range(len(obs)):
        obs_id = obs[i]['obs_id']
        obs_type = obs[i]['observation_type']
        move_names = obs[i]['move_names']
        stats = obs[i]['stats']
        base_stats = obs[i]['base_stats']
        stat_mod = obs[i]['stat_mod']
        dot = obs[i]['dot']
        heal_ot = obs[i]['heal_ot']
        revive = obs[i]['revive']
        retreat = obs[i]['retreat']
        created = LoadObservation(obs_id, obs_type)
        created.update(
            move_names,
            stats,
            base_stats,
            stat_mod,
            dot,
            heal_ot,
            revive,
            retreat
        )
        obs_objs.append(created)
        
    return obs_objs


@api_view(['GET'])
def load_obs_player(request, id):
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

    json_str = json.dumps(loaded.__dict__)
    return Response(data=json_str, status=200)


@api_view(['GET'])
def load_obs_ai(request):
    try:
        id = int(request.data.get('id'))
        hp = int(request.data.get('hp'))
        attack = int(request.data.get('attack'))
        defense = int(request.data.get('defense'))
        speed = int(request.data.get('speed'))
        evasion = int(request.data.get('evasion'))
        acc = int(request.data.get('acc'))

    except TypeError:
        return Response(status=400)

    taxa = request.data.get('type')
    
    moves = [
        request.data.get('move1'),
        request.data.get('move2'),
        request.data.get('move3'),
        request.data.get('move4')
    ]

    stats = [
        hp,
        attack,
        defense,
        speed,
        evasion,
        acc
    ]

    loaded = LoadObservation(id, taxa, moves, stats)

    json_str = json.dumps(loaded.__dict__)
    return Response(data=json_str, status=200)


@api_view(['GET'])
def create_battle(request):
    obs_objs = create_obs(request)
    battle = BattleSys.Battle(obs_objs)
    for i in range(len(battle.observations)):
        battle.observations[i] = battle.observations[i].__dict__
    json_str = json.dumps(battle.__dict__)
    return Response(data=json_str, status=200)


@api_view(['GET'])
def battle_loop(request):
    battle = recreate_battle(request)
    if battle is None:
        return Response(status=400)
    check = battle.BattleLoop(True)
    json_str = json.dumps(battle.__dict__)
    return Response(data=check, status=200+check)


@api_view(['GET'])
def get_move_name(request, index):
    battle = recreate_battle(request)
    if battle is None:
        return Response(status=400)
    name = battle.GetMoveName(index)
    json_str = json.dumps(name, indent=4)
    return Response(data=json_str, status=200)


@api_view(['GET'])
def get_flavor_text(request, index):
    battle = recreate_battle(request)
    if battle is None:
        return Response(status=400)
    flavor = battle.GetFlavorText(index)
    json_str = json.dumps(flavor)
    return Response(data=json_str, status=200)


@api_view(['GET'])
def get_bp(request, index):
    battle = recreate_battle(request)
    if battle is None:
        return Response(status=400)
    bp = battle.GetBP(index)
    json_str = json.dumps(bp)
    return Response(data=json_str, status=200)


@api_view(['GET'])
def get_acc(request, index):
    battle = recreate_battle(request)
    if battle is None:
        return Response(status=400)
    acc = battle.GetACC(index)
    json_str = json.dumps(acc, indent=4)
    return Response(data=json_str, status=200)


@api_view(['GET'])
def set_switch(request, index):
    battle = recreate_battle(request)
    if battle is None:
        return Response(status=400)
    battle.SetSwitch(index)
    json_str = json.dumps(battle.__dict__)
    return Response(data=json_str, status=200)


@api_view(['PATCH'])
def set_move_choice(request, index):
    battle = recreate_battle(request)
    if battle is None:
        return Response(status=400)
    battle.SetMoveChoice(index)
    json_str = json.dumps(battle.__dict__)
    return Response(data=json_str, status=200)


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