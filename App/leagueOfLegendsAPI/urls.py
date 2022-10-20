from django.urls import path
from . import views

urlpatterns = [
    path('<summoner>', views.summoner),
    path('', views.summonerForm)
]
