from django.shortcuts import render
from .api import API
from django.shortcuts import redirect

def summonerForm(request):
    return redirect('/summoner/'+request.POST.get('summonerName',''))

def summoner(request, summoner):
    api = API(summoner, "RGAPI-1deb906e-e98d-4fef-b67b-186f432f4c3e")
    error = api.response()
    if (error==1):
        return render(request, 'summonerError.html',{
            'error':'Summoner not exist!'
        })

    profile = api.getProfile()
    flex = api.getRanked('Flex')
    solo = api.getRanked('Solo')
    matches = api.getMatch()

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
        'matches':matches
        })