# coding=utf-8
from Rocket import *
import datetime

class Launch:
    def __init__(self, json):
        self.number = json['flight_number']
        self.name = json['mission_name'].encode('utf-8')
        self.launchpad = json['launch_site']['site_name'].encode('utf-8')
        self.details = json['details'].encode('utf-8')
        self.video = json['links']['video_link'].encode('utf-8')
        self.launchDate = json['launch_date_utc']
        self.staticFireDate = json['static_fire_date_utc']
        self.launchSuccess = json['launch_success']
        self.rocket = Rocket(json['rocket'])

    def prueba(self):
        cadena = ""
        cadena += "#" + str(self.number) + " · "  + self.name + "\n"
        cadena += self.details + "\n"
        cadena += "Launched from " + self.launchpad + "\n"
<<<<<<< HEAD
        cadena += "Launched on " + self.getLaunchDate() + "\n"
        cadena += "Static fired on " + self.getStaticFireDate() + "\n"
=======
        #cadena += "Launched on " + self.getLaunchDate() + "\n"
 #       cadena += "Static fired on " + self.getStaticFireDate() + "\n"
>>>>>>> 7a4d82f9d46d001ac9cc20666204632506e92b7e
        cadena += "Launch success: " + ("Yes" if self.launchSuccess else "No") + "\n"
        cadena += self.video + "\n"
        return cadena

    def getLaunchDate(self):
        return datetime.datetime.strptime(launchDate, "Hoy es %B %d, %Y")
    
    def getStaticFireDate(self):
        return datetime.datetime.strptime(staticFireDate, "Hoy es %B %d, %Y")