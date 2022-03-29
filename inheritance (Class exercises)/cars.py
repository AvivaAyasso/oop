from vehicles import Vehicles

class Cars (Vehicles):
    def __init__(self, color, model, wheels, year):
        super().__init__(color, model, wheels)
        self.year = year

    def getYear(self):
        return self.year

    def setYear(self, year):
        self.year = year

    def __str__(self):
        return  self.color +" "+ self.model +" "+ str(self.wheels)+" "+ str(self.year)

car1 = Cars("red", "kia", 3, 1999)
print(car1)