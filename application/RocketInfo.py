class RocketInfo:
    def __init__(self, json):
        self.id = json['rocket_id']
        self.name = json['rocket_name']
        self.description = json['description']
        self.height = json['height']['meters']
        self.diameter = json['diameter']['meters']
        self.mass = json['mass']['kg']
        self.active = json['active']
        self.reusable = json['first_stage']['reusable']
        self.firstFlight = json['first_flight']
        self.photo = json['flickr_images'][0]
        self.stages = json['stages']
        self.launchCost = json['cost_per_launch']
        self.successRate = json['success_rate_pct']
        self.engine = json['engines']['type'] + ' ' + json['engines']['version']
        self.fuel = json['engines']['propellant_2']
        self.oxidizer = json['engines']['propellant_1']

    def imprimir(self):
        cadena = ""
        cadena += "Name: " + self.name + "\n"
        cadena += self.description + "\n"
        cadena += "Hegiht: " + str(self.height) + "m" + "\n"
        cadena += "Diameter: " + str(self.diameter) + "m" + "\n"
        cadena += "Mass: " + str(self.mass) + "kg" + "\n"
        cadena += "In active: " + "yes" if self.active else "No" + "\n"
        cadena += "Reusable: " + "yes" if self.reusable else "No" + "\n"
        cadena += "Stages: " + str(self.stages) + "\n"
        cadena += "Launch cost: $" + str(self.launchCost) + "\n"
        cadena += "Success rate: " + str(self.successRate) + "%" + "\n"
        cadena += "Engine: " + self.engine + "\n"
        cadena += "Fuel: " + self.fuel + "\n"
        cadena += "Oxidizer: " + self.oxidizer + "\n"
        cadena += self.photo + "\n"
        return cadena