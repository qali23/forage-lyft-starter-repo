import unittest
from datetime import datetime

import car
from engine import CapuletEngine
from engine import WilloughbyEngine
from engine import SternmanEngine

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

class CarFactory():    
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        calliope = Car(CapuletEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date))
        return calliope
        
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        glissade = Car(WilloughbyEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date))
        return glissade

    def create_palindrome(current_date, last_service_date, warning_light_on):
        palindrome = Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date))
        return palindrome

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        rorschach = Car(WilloughbyEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date))
        return rorschach

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        thovex = Car(CapuletEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date))
        return thovex

