from vehicles import Vehicles

class Airplane(Vehicles):
    def __init__(self, wings, color, model, wheels):
        super().__init__(color, model, wheels)
        self.wings = wings

    def getWings(self):
        return self.wings

    def setWings(self, wings):
        self.wings = wings

    def __str__(self):
        return str(self.wings) +" "+ self.color +" "+ self.model +" "+ str(self.wheels)

plan1 = Airplane(2, "green", "fkkfk", 6)
print(plan1)