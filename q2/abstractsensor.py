from abc import ABC, abstractmethod

class Sensor(ABC): #abstract based class

    @abstractmethod #descriptor
    
    def get_data(self):

        pass

class TempSensor(Sensor):
    def get_data(self):
        return "24 deg C"
    def __str__(self):
        return "24 deg C"
    
sensor = TempSensor()
print(sensor)
