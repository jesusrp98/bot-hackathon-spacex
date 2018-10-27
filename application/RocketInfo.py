class RocetInfo:
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
        cadena += "Name: " + self.name
        cadena += self.description
        cadena += "Hegiht: " + str(self.height) + "m"
        cadena += "Diameter: " + str(self.diameter) + "m"
        cadena += "Mass: " + str(self.mass) + "kg"
        cadena += "In active: " + (self.active ? "Yes" : "No")
        cadena += "Reusable: " + (self.reusable ? "Yes" : "No")
        cadena += "Stages: " + self.stages
        cadena += "Launch cost: $" + self.launchCost
        cadena += "Success rate: " + self.success_rate_pct + "%"
        cadena += "Engine: " + self.engine
        cadena += "Fuel: " + self.fuel
        cadena += "Oxidizer: " + self.oxidizer
        cadena += photo
        return cadena