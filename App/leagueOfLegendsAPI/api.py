import requests
class API():
    def __init__(self, summoner, server, key):
        self.summonerName = summoner
        self.url = server
        self.key = key
        self.headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
            "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://developer.riotgames.com",
            "X-Riot-Token": key
        }

    def response(self):
        try:
            #first response
            ending = "/lol/summoner/v4/summoners/by-name/"+self.summonerName
            response = requests.get(self.url+ending, headers=self.headers)
            self.jsonFirst=response.json()

            #second response
            id=self.jsonFirst['id']
            ending="/lol/league/v4/entries/by-summoner/"+id
            response= requests.get(self.url+ending, headers=self.headers)
            self.jsonSecond=response.json()
            return 0
        except:
            return 1

    def getProfile(self):
        self.name=self.jsonFirst['name']
        self.profileIconId=self.jsonFirst['profileIconId']
        self.summonerLevel=self.jsonFirst['summonerLevel']

        return {
            'name':self.name,
            'profileIconId':self.profileIconId,
            'summonerLevel':self.summonerLevel
            }
        
    def getRanked(self, kind):
        #KIND OF TYPE GAME
        if (kind == 'Flex'):
            kind = 0
        elif (kind == 'Solo'):
            kind = 1
        else:
            kind = 0

        try:
            #SAVE VARIALBLES
            self.tier=self.jsonSecond[kind]['tier']
            self.rank=self.jsonSecond[kind]['rank']
            self.leaguePoints=self.jsonSecond[kind]['leaguePoints']
            self.wins=self.jsonSecond[kind]['wins']
            self.losses=self.jsonSecond[kind]['losses']

            #CANGE NAME TYPE OF GAME
            if (self.jsonSecond[kind]['queueType']=="RANKED_FLEX_SR"):
                self.queueType='Ranked Flex'
            elif (self.jsonSecond[kind]['queueType']=="RANKED_SOLO_5x5"):
                self.queueType='Ranked SoloQ'
            else:
                self.queueType=self.jsonSecond[kind]['queueType']

            total = self.wins+self.losses
            self.winRate = (self.wins / total)*100
            self.imagePath ='images/Emblem_{}.png'.format(self.tier)
        except:
            self.tier='NULL'
            self.rank='NULL'
            self.leaguePoints='NULL'
            self.wins=0
            self.losses=0
            self.queueType='NULL'
            self.winRate=0
            self.imagePath ='NULL'

        return {
            'tier':self.tier,
            'rank':self.rank,
            'leaguePoints':self.leaguePoints,
            'wins':self.wins,
            'losses':self.losses,
            'queueType':self.queueType,
            'winRate':self.winRate,
            'imagePath':self.imagePath
        }