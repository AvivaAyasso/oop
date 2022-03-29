from vehicles import Vehicles

class Airplane(Vehicles):
    def __init__(self, color, model, wheels, wings=2):
        super().__init__(color, model, wheels)
        self.wings = wings

    def getWings(self):
        return self.wings

    def setWings(self, wings):
        self.wings = wings

    def __str__(self):
        return self.color +" "+ self.model +" "+ str(self.wheels) +" "+ str(self.wings)

plane1 = Airplane("green", "fkkfk", 6)
print(plane1)
