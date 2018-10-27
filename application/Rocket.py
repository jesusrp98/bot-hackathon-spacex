# coding=utf-8
import Core, Fairings

class Rocket:
    def __init__(self, json_info):
        self.id = json_info['rocket_id']
        self.name = json_info['rocket_name']
        self.type = json_info['rocket_type']
        self.firstStage = self.Cores(json_info['first_stage']['cores'])
        self.secondStage = secondStage(json_info['secondStage'])
        self.fairing = Fairings(json_info['fairings'])

    def Cores(json_cores):
        list = []
        for core in json_cores:
            list.append(Core(core))

        return list




