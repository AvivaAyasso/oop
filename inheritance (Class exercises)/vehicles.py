class Vehicles:
    def __init__(self, color, model, wheels):
        self.color = color
        self.model = model
        self.wheels = wheels

        if self.wheels < 4 or self.wheels != 4:
            print("It is not possible to register a vehicle with less than four wheels.")
            self.wheels = 4
        else:
            self.wheels = self.wheels

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
        if self.wheels < 4 or self.wheels != 4:
            print("It is not possible to register a vehicle with less than four wheels.")
            self.wheels = 4
        else:
            self.wheels = self.wheels

    def __str__(self):
        return self.color +" "+ self.model +" "+ str(self.wheels)

