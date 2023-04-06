from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('introduction', views.introduction,name='introduction'),
    path('map', views.map,name='map'),
    path('help', views.help,name='help'),
    path('clue1', views.clue,name='clue1'),
    path('clue2', views.clue,name='clue2'),
    path('clue3', views.clue,name='clue3'),
    path('clue4', views.clue,name='clue4'),
    path('clue5', views.clue,name='clue5'),
    path('clue6', views.clue,name='clue6'),
    path('clue7', views.clue,name='clue7'),
    path('clue8', views.clue,name='clue8'),
    path('clue9', views.clue,name='clue9'),
    path('clue10', views.clue,name='clue10'),
    path('clue11', views.clue,name='clue11'),
    path('clue12', views.clue,name='clue12'),
]