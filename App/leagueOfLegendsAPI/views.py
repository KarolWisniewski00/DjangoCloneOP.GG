from django.shortcuts import render
import requests

def summoner(request):
    url = "https://eun1.api.riotgames.com"
    endings = "/lol/summoner/v4/summoners/by-name/WMTB"
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": "RGAPI-50fa5560-0a2c-4eb0-9793-379c2fe0351d"
    }
    
    response = requests.get(url+endings, headers=headers)
    json=response.json()
    id=json['id']
    accountId=json['accountId']
    puuid=json['puuid']
    name=json['name']
    profileIconId=json['profileIconId']
    revisionDate=json['revisionDate']
    summonerLevel=json['summonerLevel']
    endings="/lol/league/v4/entries/by-summoner/"+id
    response = requests.get(url+endings, headers=headers)
    json=response.json()
    leagueId=json[0]['leagueId']
    queueType=json[0]['queueType']
    tier=json[0]['tier']
    rank=json[0]['rank']
    leaguePoints=json[0]['leaguePoints']
    wins=json[0]['wins']
    losses=json[0]['losses']

    return render(request, 'summoner.html',{
        'id':id,
        'accountId':accountId,
        'puuid':puuid,
        'name':name,
        'profileIconId':profileIconId,
        'revisionDate':revisionDate,
        'summonerLevel':summonerLevel,
        'leagueId':leagueId,
        'queueType':queueType,
        'tier':tier,
        'rank':rank,
        'leaguePoints':leaguePoints,
        'wins':wins,
        'losses':losses,
        })