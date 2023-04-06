from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('introduction', views.introduction,name='introduction'),
    path('map', views.map,name='map'),
    path('help', views.help,name='help'),
    path('clue1', views.clue1,name='clue1'),
    path('clue2', views.clue2,name='clue2'),
    path('clue3', views.clue3,name='clue3'),
    path('clue4', views.clue4,name='clue4'),
    path('clue5', views.clue5,name='clue5'),
    path('clue6', views.clue6,name='clue6'),
    path('clue7', views.clue7,name='clue7'),
    path('clue8', views.clue8,name='clue8'),
    path('clue9', views.clue9,name='clue9'),
    path('clue10', views.clue10,name='clue10'),
    path('clue11', views.clue11,name='clue11'),
    path('clue12', views.clue12,name='clue12'),
]