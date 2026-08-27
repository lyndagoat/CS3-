class hero:
    def __init__(self, name, hp):
        self.hp = 100
        self.name = name
    def take_damage(self, amount):
        self.hp -= amount

Arthur = hero("Arthur", 100)
Morgana = hero("Morgana", 100)

Arthur.take_damage(10)

print("Arthur's HP:", Arthur.hp)
print("Morgana's HP:", Morgana.hp)
