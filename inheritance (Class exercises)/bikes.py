from vehicles import Vehicles

class Bikes (Vehicles):
    def __init__(self, trainingWheels, color, model, wheels):
        super().__init__(color, model, wheels)
        self.trainingWheels = trainingWheels

    def gettrainingWheels(self):
        return self.trainingWheels

    def settrainingWheels(self, trainingWheels):
        self.trainingWheels = trainingWheels

    def __str__(self):
        return str(self.trainingWheels) +" "+ self.color +" "+ self.model +" "+ str(self.wheels)

bike1 = Bikes(1, "pink", "kkl",5)
print(bike1)
