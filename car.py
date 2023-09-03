from abc import ABC, abstractmethod
from engine import Engine
from battery import Battery
from tire import Tire

class car(ABC):
    def __init__(self, Engine, Battery, Tire):
        self.Engine = Engine
        self.Battery = Battery
        self.Tire = Tire
    
    @abstractmethod
    def needs_service(self):
        pass
