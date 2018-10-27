class Payload:
    def __init__(self,json):
        self.id=json['payload_id']
        self.capsuleSerial = json['capsuleSerial']
        self.customer = json['customers']
        self.nationality = json['nationality']
        self.manufacturer = json['manufacturer']
        self.orbit = json['orbit']
        self.reused = json['reused']
        self.mass = json['payload_mass_kg']