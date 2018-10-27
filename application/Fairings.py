class Fairings:
    def __init__(self, json):
        self.reused = json['reused']
        self.recovery_attempt = json['recovery_attempt']
        self.recovered = json['recovered']
        self.ship = json['ship']

    def imprimir(self):
        cadena = ""
        cadena += "--------------------" + "\n"
        cadena += "Fairing reused: " + ("Yes" if self.reused else "No") + "\n"
        cadena += "Recovery attempt: " + ("Yes" if self.recovery_attempt else "No") + "\n"
        cadena += "Fairing recovered: " + ("Yes" if self.recovered else "No") + "\n"
        cadena += "Ship: " + self.ship + "\n"
        return cadena