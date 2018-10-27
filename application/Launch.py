# coding=utf-8
from Rocket import *
import datetime

class Launch:
    def __init__(self, json):
        self.number = json['flight_number']
        self.name = json['mission_name'].encode('utf-8')
        self.launchpad = json['launch_site']['site_name'].encode('utf-8')
        self.details = json['details'].encode('utf-8')
        self.video = json['links']['video_link']
        self.launchDate = json['launch_date_utc']
        self.staticFireDate = json['static_fire_date_utc']
        self.launchSuccess = json['launch_success']
        self.upcoming = json['upcoming']
        self.rocket = Rocket(json['rocket'])

    def imprimir(self):
        cadena = ""
        cadena += "#" + str(self.number) + " · "  + self.name + "\n"
        cadena += self.details + "\n"
        cadena += "Launched from " + self.launchpad + "\n"
        cadena += "Launched on " + self.launchDate.encode('utf-8') + "\n"
        cadena += "Static fired on " + self.staticFireDate.encode('utf-8') + "\n"
        cadena += "Launch success: " + ("Yes" if self.launchSuccess else "No") + "\n"
        cadena += self.rocket.imprimir().encode('utf-8')
        cadena += self.video .encode('utf-8')+ "\n"
        return cadena