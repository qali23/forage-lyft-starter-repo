from abc import ABC
from tire.tire import Tire

class CarriganTire(Tire, ABC):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        
    def needs_service(self):
        return any(val >= 0.9 for val in self.tire_wear)
