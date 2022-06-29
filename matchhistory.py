from requests import get
from json import loads

class compMatchHistory:
    def __init__(self, userName, tagName):
        self.userName = userName
        self.tagName = tagName
        self.numOfMatches = 3
        self.prevAct = ['e4a3','e4a2','e4a1']
        self.version = ['v1','v2','v3']
        self.mode = ['matches','mmr-history','mmr']
        self.mmrData = None
        self.accountData = None
        self.puuid = None
        self.region = None
        self.ranks = []
        self.mmrChange = []
        self.currentRank = None
        self.statusRequest = None    
        self.errorMsg = None   
         
    def getAccData(self) -> bool:
        if self.userName is None or self.tagName is None:
            self.errorMsg = "No User Name or Tag Name Provided"
            return False
        url = 'https://api.henrikdev.xyz/valorant/v1/account/{self.userName}/{self.tagName}'.format(self=self) 
        response = get(url)
        if self.checkErrorCode(response) is False:
            return False
        self.accountData = loads(response.text)
        return True
    
    def getMmrHistory(self) -> bool:
        if self.puuid == None or self.region == None or self.version == None:
            return False
        url = 'https://api.henrikdev.xyz/valorant/{self.version[0]}/by-puuid/{self.mode[1]}/{self.region}/{self.puuid}'.format(self=self) 
        response = get(url)
        if self.checkErrorCode(response) is False:
            return False
        self.mmrData = loads(response.text)
        return True
    
    def getPrevMmr(self) -> bool:
        if self.puuid == None or self.region == None or self.version == None:
            return False
        
        for i in range(3):
            act = self.prevAct[i]
            url = 'https://api.henrikdev.xyz/valorant/{self.version[1]}/by-puuid/{self.mode[2]}/{self.region}/{self.puuid}?filter={act}'.format(self=self, act=act) 
            response = get(url)
            
            if response.status_code == 500:
                self.ranks.append('Unranked')
            else:
                if self.checkErrorCode(response) is False:
                    return False
                res = loads(response.text)
                data = res['data']['final_rank_patched']
                self.ranks.append(data)
        return True
    
    def formatAccData(self) -> bool:
        if self.accountData is None:
            return False
        if bool(self.accountData['data']) is False:
            self.errorMsg = 'No Account Information Available'
            return False
        
        accData = self.accountData['data']
        self.puuid = accData['puuid']
        self.region = accData['region']
        
        return True
        
    def formatMmrData(self) -> bool:
        if self.mmrData is None:
            return False
        if bool(self.mmrData['data']) is False:
            self.errorMsg = 'No MMR Information Available'
            return False
        
        
        for i in range(3):
            if len(self.mmrData['data']) <= i:
                self.mmrChange.append('Unranked')
                break
            
            data = self.mmrData['data'][i]
            self.mmrChange.append(data['mmr_change_to_last_game'])
            self.currentRank = data['currenttierpatched']
            
        return True
        
    def checkErrorCode(self, jsonData) -> bool:
        jsonStr = loads(jsonData.text)
        statusCondition = jsonStr['status']
        self.statusRequest = statusCondition
        if statusCondition != 200 | statusCondition != 0:
            errorMsg = jsonStr['message']
            self.errorMsg = errorMsg
            print('{}: {}'.format(statusCondition, errorMsg))
            return False
        else:
            return True


def main():
    mh = compMatchHistory('Lifended', '4188')
    
    # if mh.getAccData() is True:
    #     if mh.formatAccData() is True:
    #         if mh.getMmrHistory() is True:
    #             if mh.formatMmrData() is True:
    #                 if mh.getPrevMmr() is True:
    #                     counter = 1
    #                     for x in mh.ranks:
    #                         print("For episode 4 act {actInfo}: {rank}".format(actInfo=counter, rank=x))
    #                         counter = counter+1
                        
    #                     print()
    #                     counter = 1
    #                     for x in mh.mmrChange:
    #                         print("For match {counter}: {mmr}".format(counter=counter, mmr=x))
    #                         counter = counter+1
                        
    #                     print()
    #                     print('{user}\'s current rank is: {rank}'.format(user=mh.userName, rank = mh.currentRank))
                
    
    
    
    
    
if __name__ == '__main__':
    main()  
        

