import os, requests

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect

from rest_framework import generics, status
from rest_framework.exceptions import NotFound

from .serializers import PlayerSerializer, ObsSerializer
from .models import Player, Observation

from .forms import LoginForm
from dotenv import load_dotenv

from pyinaturalist.auth import get_access_token

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

            request.session["username"] = form.cleaned_data['username']
            return redirect('/?username=' + form.cleaned_data['username'])
    else:
        form = LoginForm()

    return render(request, 'backend/login.html', {'form': form})


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