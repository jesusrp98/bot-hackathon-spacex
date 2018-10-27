class Payload:
    def __init__(self, json):
        self.id = json['payload_id']
        self.customer = json['customers'][0]
        self.nationality = json['nationality']
        self.manufacturer = json['manufacturer']
        self.orbit = json['orbit']
        self.mass = json['payload_mass_kg']

    def imprimir(self):
        cadena = ""
        cadena += "--------------------" + "\n"
        cadena += "Payload: " + self.payload_id + "\n"
        cadena += "Customer: " + self.customer + "\n"
        cadena += "Nationality: " + self.nationality + "\n"
        cadena += "Orbit: " + self.orbit + "\n"
        cadena += "Mass: " + str(self.mass) + "\n"
        return cadena