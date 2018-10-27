import Payload

class SecondStage:
    def __init__(self, json):
        self.block = json['block']
        self.payload = createPayload(json)
    
    def createPayload(json):
        list = []
        for payload in json:
            list.append(Payload(payload))

        return list