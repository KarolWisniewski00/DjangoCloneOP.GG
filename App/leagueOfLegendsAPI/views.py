from django.shortcuts import render
import requests

def summoner(request):
    #THIS DATA WILL BE TAKE FROM FORM
    summonerName = "WMTB"
    url = "https://eun1.api.riotgames.com"
    key = "RGAPI-b1b79aa7-aece-4aba-8c63-f2a68577795b"

    #GET DATA FROM API
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": key
    }
    #first response
    endingFirst = "/lol/summoner/v4/summoners/by-name/"+summonerName
    responseFirst = requests.get(url+endingFirst, headers=headers)
    jsonFirst=responseFirst.json()

    #second response
    id=jsonFirst['id']
    endingSecond="/lol/league/v4/entries/by-summoner/"+id
    responseSecond = requests.get(url+endingSecond, headers=headers)
    jsonSecond=responseSecond.json()

    #SAVE DATA TO THE VARIABLES
    name=jsonFirst['name']
    profileIconId=jsonFirst['profileIconId']
    summonerLevel=jsonFirst['summonerLevel']
    
    #FLEX RANKED GET DATA
    tierFlex=jsonSecond[0]['tier']
    rankFlex=jsonSecond[0]['rank']
    leaguePointsFlex=jsonSecond[0]['leaguePoints']
    winsFlex=jsonSecond[0]['wins']
    lossesFlex=jsonSecond[0]['losses']

    #FLEX RANKED FUNCTIONS
    #change name
    if (jsonSecond[0]['queueType']=="RANKED_FLEX_SR"):
        queueTypeFlex='Ranked Flex'
    else:
        queueTypeFlex=jsonSecond[0]['queueType']
    #winrate
    totalFlex = winsFlex+lossesFlex
    winRateFlex = (winsFlex / totalFlex)*100

    #SOLO RANKED GET DATA
    tierSolo=jsonSecond[1]['tier']
    rankSolo=jsonSecond[1]['rank']
    leaguePointsSolo=jsonSecond[1]['leaguePoints']
    winsSolo=jsonSecond[1]['wins']
    lossesSolo=jsonSecond[1]['losses']

    #SOLO RANKED FUNCTIONS
    #change name
    if (jsonSecond[1]['queueType']=="RANKED_SOLO_5x5"):
        queueTypeSolo='Ranked SoloQ'
    else:
        queueTypeSolo=jsonSecond[1]['queueType']
    #winrate
    totalSolo = winsSolo+lossesSolo
    winRateSolo = (winsSolo / totalSolo)*100

    return render(request, 'summoner.html',{
        'id':id,
        'name':name,
        'profileIconId':profileIconId,
        'summonerLevel':summonerLevel,
        'queueTypeFlex':queueTypeFlex,
        'tierFlex':tierFlex,
        'rankFlex':rankFlex,
        'leaguePointsFlex':leaguePointsFlex,
        'winsFlex':winsFlex,
        'lossesFlex':lossesFlex,
        'winRateFlex':'{:0.2f}'.format(winRateFlex),
        'queueTypeSolo':queueTypeSolo,
        'tierSolo':tierSolo,
        'rankSolo':rankSolo,
        'leaguePointsSolo':leaguePointsSolo,
        'winsSolo':winsSolo,
        'lossesSolo':lossesSolo,
        'winRateSolo': '{:0.2f}'.format(winRateSolo),
        })