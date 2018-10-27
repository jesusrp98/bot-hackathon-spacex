# coding=utf-8
from Core import *
from Fairings import *
from SecondStage import *

class Rocket:
    def __init__(self, json_info):
        self.name = json_info['rocket_name']
        self.firstStage = self.Cores(json_info['first_stage']['cores'])
        self.secondStage = SecondStage(json_info['second_stage'])
        self.fairing = Fairings(json_info['fairings'])

    def Cores(self, json_cores):
        list = []
        for core in json_cores:
            list.append(Core(core))

        return list

    def imprimir(self):
        cadena = ""
        cadena += "--------------------" + "\n"
        cadena += "Rocket name: " + self.name + "\n"
        for core in self.firstStage:
            cadena += core.imprimir()
        cadena += self.secondStage.imprimir()
        cadena += self.fairing.imprimir()
        return cadena