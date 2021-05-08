"""naturesrpg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from .views import ObsDetail, ObsList, PlayerDetail, PlayerList, login, load_obs, create_battle, battle_loop, get_move_name, get_flavor_text, get_bp, get_acc, set_switch, set_move_choice
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('login/', login),
    path('players/', PlayerList.as_view(), name='players'),
    path('players/<int:pk>/', PlayerDetail.as_view(), name='player'),
    path('obs/<int:owner>/', ObsList.as_view(), name='observations'),
    path('obs/<int:owner>/<int:obs>/', ObsDetail.as_view(), name='observation'),
    path('loadobs/<int:id>/', load_obs),
    path('createbattle/', create_battle),
    path('battle/', battle_loop),
    path('movename/', get_move_name),
    path('textflavor/<int:index>/', get_flavor_text),
    path('bp/<int:index>/', get_bp),
    path('get_acc/<int:index>/', get_acc),
    path('switch/<int:index>', set_switch),
    path('movechoice/<int:index>/', set_move_choice)
]

urlpatterns = format_suffix_patterns(urlpatterns)