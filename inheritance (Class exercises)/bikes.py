from vehicles import Vehicles

class Bikes (Vehicles):
    def __init__(self, trainingWheels):
        super().__init__()
        self.trainingWheels = trainingWheels

    def gettrainingWheels(self):
        return self.trainingWheels

    def settrainingWheels(self, trainingWheels):
        self.trainingWheels = trainingWheels

    def __str__(self):
        return self.trainingWheels +" "+ self.color+" "+ self.model+" "+ str(self.wheels)
