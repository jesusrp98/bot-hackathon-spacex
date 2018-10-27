from Rocket import *
from datetime import datetime

class Launch:
    def __init__(self, json):
        self.number = json['flight_number']
        self.name = json['mission_name'].encode('utf-8')
        self.launchpad = json['launch_site']['site_name']
        self.details = json['details']
        self.video = json['links']['video_link']
        self.launchDate = json['launch_date_utc']
        self.staticFireDate = json['static_fire_date_utc']
        self.launchSuccess = json['launch_success']
        self.rocket = Rocket(json['rocket'])

    def prueba(self):
        cadena = ""
        cadena += "#" + str(self.number) + " · "  + self.name + "\n"
        cadena += self.details + "\n"
        cadena += "Launched from " + self.launchpad + "\n"
        cadena += "Launched on " + getLaunchDate() + "\n"
        cadena += "Static fired on " + getStaticFireDate() + "\n"
        cadena += "Launch success: " + "Yes" if self.launchSuccess else "No" + "\n"
        cadena += self.video + "\n"
        return cadena

    def getLaunchDate(self):
        return datetime(launchDate).strftime("%a, %d %b %Y %H:%M:%S")
    
    def getStaticFireDate(self):
        return datetime(staticFireDate).strftime("%a, %d %b %Y %H:%M:%S")