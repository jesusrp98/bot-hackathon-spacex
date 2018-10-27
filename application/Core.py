class Core:
    def __init__(self, json):
        self.id = json['core_serial']
        self.landingType = json['landing_type']
        self.landingZone = json['landing_vehicle']
        self.reused = json['reused']
        self.landingSuccess = json['reused']
        self.landingIntent = json['landing_intent']
        self.block = json['block']
        self.flights = json['flight']

    def imprimir(self):
        cadena = ""
        cadena += "--------------------" + "\n"
        cadena += "Core serial: " + str(self.id) + "\n"
        cadena += "Landing type: " + self.landingType + "\n"
        cadena += "Landing zone: " + self.landingZone + "\n"
        cadena += "Reused: " + ("Yes" if self.reused else "No") + "\n"
        cadena += "Landing success: " + ("Yes" if self.landingSuccess else "No") + "\n"
        cadena += "Landing intent: " + ("Yes" if self.landingIntent else "No") + "\n"
        cadena += "Block: " + str(self.block) +  "\n"
        cadena += "Flights: " + str(self.flights) +  "\n"
        return cadena