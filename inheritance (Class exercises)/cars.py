from vehicles import Vehicles

class Cars (Vehicles):
    def __init__(self, year, color, model, wheels):
        super().__init__(color, model, wheels)
        self.year = year

    def getYear(self):
        return self.year

    def setYear(self, year):
        self.year = year

    def __str__(self):
        return str(self.year) +" "+ self.color +" "+ self.model +" "+ str(self.wheels)

