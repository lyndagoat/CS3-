class Glassware:
    
    def __init__(self):
        pass
    
class Beaker(Glassware):

    def __init__(self, capacityInml = 250):
        super().__init__()
        self.capacityInml = capacityInml
                 
class Tray:
    
    def __init__(self):
        self.beakers = [Beaker() for i in range(5)]

myTray = Tray()
print(f"Tray created with {len(myTray.beakers)} beakers.")
