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
from .views import ObsDetail, ObsList, PlayerDetail, PlayerList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('players/', PlayerList.as_view(), name='players'),
    path('players/<int:pk>/', PlayerDetail.as_view(), name='player'),
    path('obs/<int:owner>/', ObsList.as_view(), name='observations'),
    path('obs/<int:owner>/<int:obs>/', ObsDetail.as_view(), name='observation')
]

urlpatterns = format_suffix_patterns(urlpatterns)