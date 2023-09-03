import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


#Variables to contain all the varying values depending on which test is being run
#To prevent code repetition
current_date = datetime.today().date()
last_service_date = [current_date,
                     current_date.replace(year=current_date.year - 1),
                     current_date.replace(year=current_date.year - 3),
                     current_date.replace(year=current_date.year - 5)]
current_mileage = [0,30000,30001,60000,60001]
last_service_mileage = 0
warning_light_is_on = [True, False]

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        calliope = car(CapuletEngine(last_service_mileage, current_mileage[0]),SpindlerBattery(last_service_date[2], current_date))
        self.assertTrue(calliope.needs_service())

    def test_battery_should_not_be_serviced(self):
        calliope = car(CapuletEngine(last_service_mileage, current_mileage[0]),SpindlerBattery(last_service_date[1], current_date))
        self.assertFalse(calliope.needs_service())

    def test_engine_should_be_serviced(self):
        calliope = car(CapuletEngine(last_service_mileage, current_mileage[2]),SpindlerBattery(last_service_date[0], current_date))
        self.assertTrue(calliope.needs_service())

    def test_engine_should_not_be_serviced(self):
        calliope = car(CapuletEngine(last_service_mileage, current_mileage[1]),SpindlerBattery(last_service_date[0], current_date))
        self.assertFalse(calliope.needs_service())

class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        glissade = car(WilloughbyEngine(last_service_mileage, current_mileage[0]),SpindlerBattery(last_service_date[2], current_date))
        self.assertTrue(glissade.needs_service())

    def test_battery_should_not_be_serviced(self):
        glissade = car(WilloughbyEngine(last_service_mileage, current_mileage[0]),SpindlerBattery(last_service_date[1], current_date))
        self.assertFalse(glissade.needs_service())

    def test_engine_should_be_serviced(self):
        glissade = car(WilloughbyEngine(last_service_mileage, current_mileage[4]),SpindlerBattery(last_service_date[0], current_date))
        self.assertTrue(glissade.needs_service())

    def test_engine_should_not_be_serviced(self):
        glissade = car(WilloughbyEngine(last_service_mileage, current_mileage[3]),SpindlerBattery(last_service_date[0], current_date))
        self.assertFalse(glissade.needs_service())

class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        palindrome = car(SternmanEngine(warning_light_on[1]),SpindlerBattery(last_service_date[2], current_date))
        self.assertTrue(palindrome.needs_service())

    def test_battery_should_not_be_serviced(self):
        palindrome = car(SternmanEngine(warning_light_on[1]),SpindlerBattery(last_service_date[1], current_date))
        self.assertFalse(palindrome.needs_service())

    def test_engine_should_be_serviced(self):
        palindrome = car(SternmanEngine(warning_light_on[0]),SpindlerBattery(last_service_date[0], current_date))
        self.assertTrue(palindrome.needs_service())

    def test_engine_should_not_be_serviced(self):
        palindrome = car(SternmanEngine(warning_light_on[1]),SpindlerBattery(last_service_date[0], current_date))
        self.assertFalse(palindrome.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        rorschach = car(WilloughbyEngine(last_service_mileage, current_mileage[0]),NubbinBattery(last_service_date[3], current_date))
        self.assertTrue(rorschach.needs_service())

    def test_battery_should_not_be_serviced(self):
        rorschach = car(WilloughbyEngine(last_service_mileage, current_mileage[0]),NubbinBattery(last_service_date[2], current_date))
        self.assertFalse(rorschach.needs_service())

    def test_engine_should_be_serviced(self):
        rorschach = car(WilloughbyEngine(last_service_mileage, current_mileage[4]),NubbinBattery(last_service_date[0], current_date))
        self.assertTrue(rorschach.needs_service())

    def test_engine_should_not_be_serviced(self):
        rorschach = car(WilloughbyEngine(last_service_mileage, current_mileage[3]),NubbinBattery(last_service_date[0], current_date))
        self.assertFalse(rorschach.needs_service())

class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        thovex = car(CapuletEngine(last_service_mileage, current_mileage[0]),NubbinBattery(last_service_date[3], current_date))
        self.assertTrue(thovex.needs_service())

    def test_battery_should_not_be_serviced(self):
        thovex = car(CapuletEngine(last_service_mileage, current_mileage[0]),NubbinBattery(last_service_date[2], current_date))
        self.assertFalse(thovex.needs_service())

    def test_engine_should_be_serviced(self):
        thovex = car(CapuletEngine(last_service_mileage, current_mileage[2]),NubbinBattery(last_service_date[0], current_date))
        self.assertTrue(thovex.needs_service())

    def test_engine_should_not_be_serviced(self):
        thovex = car(CapuletEngine(last_service_mileage, current_mileage[1]),NubbinBattery(last_service_date[0], current_date))
        self.assertFalse(thovex.needs_service())


if __name__ == '__main__':
    unittest.main()
