import Payload

class SecondStage:
    def __init__(def, json):
        self.block = json['block']
        self.payload = createPyaload(json)
    
    def createPyaload(json):
        list = []
        for payload in json:
            list.append(Payload(payload))
        return list