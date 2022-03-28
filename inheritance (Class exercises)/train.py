from vehicles import Vehicles

class Train (Vehicles):
    def __init__(self, carriage):
        super().__init__()
        self.carriage = carriage

    def getCarriage(self):
        return self.carriage

    def setCarriage(self, carriage):
        self.carriage = carriage

    def __str__(self):
        return str(self.carriage) +" "+ self.color +" "+ self.model +" "+ str(self.wheels)