from abc import ABC, abstractmethod

class Sensor(ABC):

    @abstractmethod

    def get_reading(self):
        pass
    
class PHSensor(Sensor):
    def get_reading(self):
        return "7.2 pH (Neutral)"
    def __str__(self):
        return "7.2 pH (Neutral)"

class TempSensor(Sensor):
    def get_reading(self):
        return "24.5 °C"
    def __str__(self):
        return "24.5 °C"

phSensor = PHSensor()
tempSensor = TempSensor()
print("--- Lab Inventory System ---")
print("[pH Sensor] Reading:", phSensor)
print("[Temperature Sensor] Reading:", tempSensor)
