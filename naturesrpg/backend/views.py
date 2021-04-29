from rest_framework import generics, status
from rest_framework.exceptions import NotFound

from .serializers import PlayerSerializer, ObsSerializer
from .models import Player, Observation


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