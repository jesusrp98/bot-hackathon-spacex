class Fairings:
    def __init__(self, json):
        self.reused = json['reused']
        self.recovery_attempt = json['recovery_attempt']
        self.recovered = json['recovered']
        self.ship = json['ship']