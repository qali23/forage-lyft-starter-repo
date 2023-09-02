from abc import ABC, abstractmethod
from engine import Engine
from battery import Battery

class car(ABC):
    def __init__(self, Engine, Battery):
        self.Engine = Engine
        self.Battery = Battery
    
    @abstractmethod
    def needs_service(self):
        pass
