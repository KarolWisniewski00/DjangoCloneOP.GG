from django.shortcuts import render
from .api import API

def summoner(request, summoner):
    api = API(summoner, "https://eun1.api.riotgames.com", "RGAPI-ad0165a1-44f6-4548-9b62-951287bcffb4")
    error = api.response()
    if (error==1):
        return render(request, 'summonerError.html',{
            'error':'Summoner not exist!'
        })

    profile = api.getProfile()
    flex = api.getRanked('Flex')
    solo = api.getRanked('Solo')

    return render(request, 'summoner.html',{
        'name':profile['name'],
        'profileIconId':profile['profileIconId'],
        'summonerLevel':profile['summonerLevel'],
        'queueTypeFlex':flex['queueType'],
        'tierFlex':flex['tier'],
        'rankFlex':flex['rank'],
        'leaguePointsFlex':flex['leaguePoints'],
        'winsFlex':flex['wins'],
        'lossesFlex':flex['losses'],
        'winRateFlex':'{:0.2f}'.format(flex['winRate']),
        'imagePathFlex':flex['imagePath'],
        'queueTypeSolo':solo['queueType'],
        'tierSolo':solo['tier'],
        'rankSolo':solo['rank'],
        'leaguePointsSolo':solo['leaguePoints'],
        'winsSolo':solo['wins'],
        'lossesSolo':solo['losses'],
        'winRateSolo': '{:0.2f}'.format(solo['winRate']),
        'imagePathSolo':solo['imagePath'],
        })