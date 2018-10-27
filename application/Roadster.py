# coding=utf-8
class Roadster:
    def __init__(self, json):
        self.name = "Tesla Roadster"
        self.description = json['details']
        self.mass = json['launch_mass_kg']
        self.firstFlight = json['launch_date_utc']
        self.photo = json['flickr_images'][0]
        self.orbit = json['orbit_type']
        self.apoapsis = json['apoapsis_au']
        self.periapsis = json['periapsis_au']
        self.inclination = json['inclination']
        self.longitude = json['longitude']
        self.period = json['period']
        self.speed = json['speed_kph']
        self.earthDistance = json['earth_distance_km']
        self.marsDistance = json['mars_distance_km']

    def imprimir(self):
        cadena = ""
        cadena += self.name + "\n"
        cadena += self.description + "\n"
        cadena += "Mass: " + str(self.mass) + "\n"
        cadena += "Launched on: " + str(self.firstFlight) + "\n"
        cadena += "Orbit: " + str(self.orbit) + "\n"
        cadena += "Apoapsis: " + str(self.apoapsis_au) + " ua" + "\n"
        cadena += "Periapsis: " + str(self.periapsis_au) + " ua" + "\n"
        cadena += "Inclination: " + str(self.inclination)  + "ª" + "\n"
        cadena += "Longitude: " + str(self.longitude)  + "ª" + "\n"
        cadena += "Period: " + str(self.period)  + " days" + "\n"
        cadena += "Speed: " + str(self.speed)  + " km/h" + "\n"
        cadena += "Earth distance: " + str(self.earthDistance)  + " km" + "\n"
        cadena += "Mars distance: " + str(self.marsDistance)  + " km" + "\n"
        cadena += self.photo
        return cadena