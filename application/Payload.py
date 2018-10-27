class Payload:
    def __init__(self, json):
        self.id = json['payload_id']
        self.customer = json['customers'][0]
        self.nationality = json['nationality']
        self.manufacturer = json['manufacturer']
        self.orbit = json['orbit']
        self.reused = json['reused']
        self.mass = json['payload_mass_kg']