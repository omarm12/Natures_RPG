from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
# class login(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         content = {
#             'user': str(request.user),
#             'auth': str(request.auth)
#         }
#         return Response("https://www.inaturalist.org/login")
def login(request):
    return HttpResponseRedirect("https://www.inaturalist.org/login")