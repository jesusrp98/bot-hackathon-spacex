from Rocket import *


class Launch:
    def __init__(self, json):
        self.number = json['flight_number']
        self.name = json['mission_name'].encode('utf-8')
        self.launchpad = json['launch_site']['site_name']
        self.details = json['details']
        self.video = json['links']['video_link']
        self.launchDate = json['launch_date_local']
        self.staticFireDate = json['static_fire_date_utc']
        self.launchSuccess = json['launch_success']
        self.rocket = Rocket(json['rocket'])

    def prueba(self):
        cadena = ""
        cadena += "#" + str(self.number) + " · "  + self.name + "\n"
        cadena += self.details + "\n"
        cadena += "Launched from " + self.launchpadName + "\n"
        cadena += "Launched on " + self.launchDate + "\n"
        cadena += "Static fired on " + self.staticFireDate + "\n"
        cadena += isLaunchedSuccess() + "\n"
        cadena += self.video + "\n"
        return cadena

    def isLaunchedSuccess(self):
        return "Yes" if self.launchSuccess else "No"