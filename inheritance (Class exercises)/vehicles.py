class Vehicles:
    def __init__(self, color, model, wheels):
        self.color = color
        self.model = model
        self.wheels = wheels

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getModel(self):
        return self.model

    def setModel(self, model):
        self.model = model

    def getWheels(self):
        return self.wheels

    def setWheels(self, wheels):
        self.wheels = wheels

    def numOfWheel(self):
        if self.wheels < 2 or self.wheels != 2:
            print("It is not possible to register a vehicle with less than four wheels.")
            self.__wheels = 4

    def __str__(self):
        return self.color +" "+ self.model+" "+ str(self.wheels)
