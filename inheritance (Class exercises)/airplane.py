from vehicles import Vehicles

class Airplane(Vehicles):
    def __init__(self, wings):
        super().__init__()
        self.wings = wings

    def getWings(self):
        return self.wings

    def setWings(self, wings):
        self.wings = wings

    def __str__(self):
        return str(self.wings) +" "+ self.color +" "+ self.model +" "+ str(self.wheels)