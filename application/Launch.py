from Rocket import *


class Launch:
    def __init__(self, json):
        self.number = json['flight_number']
        self.name = json['mission_name'].encode('utf-8')
        self.launchpadId = json['launch_site']['site_id']
        self.launchpadName = json['launch_site']['site_name']
        self.imageUrl = json['links']['mission_patch_small']
        self.details = json['details']
        self.tentativePrecision = json['tentative_max_precision']
        self.video = json['links']['video_link']
        self.launchDate = json['launch_date_local']
        self.staticFireDate = json['static_fire_date_utc']
        self.launchSuccess = json['launch_success']
        self.rocket = Rocket(json['rocket'])

    def prueba(self):
        cadena=""
        cadena = cadena + "Number: " + str(self.number) + "\n"
        #print(self.number)
        cadena = cadena + "Name: " + self.name + "\n"
        #print(self.name)
        cadena = cadena + "LaunchpadId: " + self.launchpadId + "\n"
        #print(self.launchpadId)
        cadena = cadena + "launchpadName: " + self.launchpadName + "\n"
        #print(self.launchpadName)
        #print(self.imageUrl)
        cadena = cadena + "details: " + self.details + "\n"
        #print(self.details)
        cadena = cadena + "tentativePrecision: " + self.tentativePrecision + "\n"
        #print(self.tentativePrecision)
        #print(self.video)
        cadena = cadena + "launchDate: " + self.launchDate + "\n"
        #print(self.launchDate)
        cadena = cadena + "staticFireDate: " + self.staticFireDate + "\n"
        #print(self.staticFireDate)
        if self.launchSuccess==True:
            cadena = cadena + "launchSuccess: " + "Yes" + "\n"
        else:
            cadena = cadena + "launchSuccess: " + "No" + "\n"
        cadena = cadena + self.video + "\n"
        #print(self.launchSuccess)
        #cadena = cadena + "rocket: " + self.rocket + "\n"
        #print(self.rocket)

        return cadena