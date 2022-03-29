from vehicles import Vehicles

class Bikes (Vehicles):
    def __init__(self, color, model, wheels, trainingWheels, ):
        super().__init__(color, model, wheels)
        self.trainingWheels = trainingWheels

    def gettrainingWheels(self):
        return self.trainingWheels

    def settrainingWheels(self, trainingWheels):
        self.trainingWheels = trainingWheels

    def __str__(self):
        return  self.color +" "+ self.model +" "+ str(self.wheels) +" "+ str(self.trainingWheels)

bike1 = Bikes("pink", "kkl", 1, 1)
print(bike1)
