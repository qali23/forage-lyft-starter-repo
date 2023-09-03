import unittest
from datetime import datetime

import car
from engine import CapuletEngine
from engine import WilloughbyEngine
from engine import SternmanEngine

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

from tire.Tire import Tire
from tire.CarriganTire import CarriganTire
from tire.OctoprimeTire import OctoprimeTire

class CarFactory():    
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, Tire t):
        calliope = Car(CapuletEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date), t)
        return calliope
        
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, Tire t):
        glissade = Car(WilloughbyEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date), t)
        return glissade

    def create_palindrome(current_date, last_service_date, warning_light_on, Tire t):
        palindrome = Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date), t)
        return palindrome

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, Tire t):
        rorschach = Car(WilloughbyEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date), t)
        return rorschach

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, Tire t):
        thovex = Car(CapuletEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date), t)
        return thovex

