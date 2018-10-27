from Payload import *

class SecondStage:
    def __init__(self, json):
        self.block = json['block']
        self.payloads = self.createPayload(json['payloads'])
    
    def createPayload(self, json):
        list = []
        for payload in json:
            list.append(Payload(payload))
        return list

    def imprimir(self):
        cadena = ""
        cadena += "--------------------" + "\n"
        cadena += "Block: " + str(self.block) + "\n"
        for payload in payloads
            cadena += payload.imprimir()
        return cadena