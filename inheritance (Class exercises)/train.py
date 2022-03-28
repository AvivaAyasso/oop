from vehicles import Vehicles

class Train (Vehicles):
    def __init__(self, carriage=20, color="red", model="mian", wheels=40):
        super().__init__(color, model, wheels)
        self.carriage = carriage

    def getCarriage(self):
        return self.carriage

    def setCarriage(self, carriage):
        self.carriage = carriage

    def __str__(self):
        return str(self.carriage) +" "+ self.color +" "+ self.model +" "+ str(self.wheels)

train1 = Train()
print(train1)