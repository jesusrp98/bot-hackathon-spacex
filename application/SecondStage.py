from Payload import *

class SecondStage:
    def __init__(self, json):
        self.block = json['block']
        self.payload = self.createPayload(json)
    
    def createPayload(self, json):
        list = []
        for payload in json:
            list.append(Payload(payload))

        return list