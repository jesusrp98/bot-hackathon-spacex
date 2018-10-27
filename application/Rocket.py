# coding=utf-8
from Core import *
from Fairings import *
from SecondStage import *

class Rocket:
    def __init__(self, json_info):
        self.id = json_info['rocket_id']
        self.name = json_info['rocket_name']
        self.type = json_info['rocket_type']
        self.firstStage = self.Cores(json_info['first_stage']['cores'])
        self.secondStage = SecondStage(json_info['second_stage'])
        self.fairing = Fairings(json_info['fairings'])

    def Cores(self, json_cores):
        list = []
        for core in json_cores:
            list.append(Core(core))

        return list




