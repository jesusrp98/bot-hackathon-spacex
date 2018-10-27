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