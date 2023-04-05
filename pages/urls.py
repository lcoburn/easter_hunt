from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('introduction', views.introduction,name='introduction'),
    path('help', views.help,name='help'),
]