class Unit:
    def __init__(self, name, ip_address):
        self.name = name
        self.ip_address = ip_address

    def turn_on_off(self):
        print("wpisz ON żeby włączyć lub OFF żeby wyłączyć")
        mode = input().upper()
        print(f"Urządzenie {self.name} o adresie IP: {self.ip_address} jest w trybie {mode}")


ESU40 = Unit("ESU40", "196.254.112.102")
ESU40.turn_on_off()

SMF100A = Unit("SMF100A", "196.254.98.2")
SMF100A.turn_on_off()