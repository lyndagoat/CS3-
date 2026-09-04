class Lab:
    def __init__(self, room_number):
        self.room_number = room_number 

class Technician:
    def __init__(self, name):
        self.name = name
        self.assigned_lab = None

    def assign_lab(self, lab_obj):
        self.assigned_lab = lab_obj

physics_lab = Lab("Room 303")

mr_allin = Technician("Mr. Allin")

mr_allin.assign_lab(physics_lab)

print(mr_allin.assigned_lab.room_number)
