from vehicles import Vehicles

class Train (Vehicles):
    def __init__(self, color, model, wheels, carriage=20):
        super().__init__(color, model, wheels)
        self.carriage = carriage

    def getCarriage(self):
        return self.carriage

    def setCarriage(self, carriage):
        self.carriage = carriage

    def __str__(self):
        return self.color +" "+ self.model +" "+ str(self.wheels) +" "+ str(self.carriage)

train1 = Train("pink", "kkk", 40)
print(train1)
