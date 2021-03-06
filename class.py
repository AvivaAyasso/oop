class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def getname (self):
        return self.__name

    def setname (self, name):
        self.__name = name

    def getage(self):
        return self.__age

    def setage(self, age):
        self.__age = age


    def __str__(self):
        return self.__name+str(self.__age)


student1 = Student("aviva", 30)
student2 = Student("betty", 23)
print(student1)
print(student2)
print(student2.getname())
student2.setname("rivka")
print(student2.getname())




class Cars:
    def __init__(self, wheels, model, year, price):
        self.__wheels = wheels
        self.__model = model
        self.__year = year
        self.__price = price

        if self.__wheels < 4 or self.__wheels != 4:
            print("It is not possible to register a vehicle with less than four wheels.")
            self.__wheels = 4
        else:
            self.__wheels = self.__wheels


    def getwheels(self):
        return self.__wheels

    def setwheels(self, wheels):
        if self.__wheels < 4 or self.__wheels != 4:
            print("It is not possible to register a vehicle with less than four wheels.")
            self.__wheels = 4
        else:
            self.__wheels = self.__wheels

    def getmodel(self):
        return self.__model

    def setmodel(self, model):
        self.__model = model

    def getyear(self):
        return self.__year

    def setyear(self, year):
        self.__year = year

    def getprice(self):
        return self.__price

    def setprice(self, price):
        self.__price = price

    def __str__(self):
        return str(self.__wheels)+" "+str(self.__year)+" "+str(self.__price)+" "+self.__model


car1 = Cars(3, "kia sportage", 2003, 25000)
car2 = Cars(4, "Hyundai", 2011, 35000)
car3 = Cars(6, "Hyundai", 2009, 24000)
print(max(car1.getprice(), car2.getprice(), car3.getprice()))

print(car1, car3)

# class Exercises

#1
class Circel:
    def __init__(self, area=25, color="red"):
        self.__area = area
        self.__color = color

    def getarea(self):
        return self.__area

    def setarea(self, area):
        self.__area = area

    def getcolor(self):
        return self.__color

    def setcolor(self, color):
        self.__color = color

    def __str__(self):
        return str(self.__area)+" " + self.__color


class Square:
    def __init__(self, sarea=30, scolor="green"):
        self.__sarea = sarea
        self.__scolor = scolor

    def getarea(self):
        return self.__sarea

    def setarea(self, sarea):
        self.__sarea = sarea

    def getcolor(self):
        return self.__scolor

    def setcolor(self, scolor):
            self.__scolor = scolor

    def __str__(self):
        return str(self.__sarea) + " " + self.__scolor

circel1 = Circel(70, "blue")
circel2 = Circel()

square1 = Square()
square2 = Square(90, "red")

print(circel1)
print(circel2)
print(square1)
print(square2)

#2
class Home:
    def __init__(self, address, home_number, buying_price, rent_price):
        self.__address = address
        self.__home_number = home_number
        self.__buying_price = buying_price
        self.__rent_price = rent_price

    def getaddress(self):
        return self.__address

    def setaddress(self, address):
        self.__address = address

    def gethome_number(self):
        return self.__home_number

    def sethome_number(self, home_number):
        self.__home_number = home_number

    def getbuying_price(self):
        return self.__buying_price

    def setbuying_price(self, buying_price):
        self.__buying_price = buying_price

    def getrent_price(self):
        return self.__rent_price

    def setrent_price(self, rent_price):
        self.__rent_price = rent_price

    def tshua(self):
        return (self.__rent_price * 12 // self.__buying_price) * 100

    def __str__(self):
        return self.__address +" "+ str(self.__home_number) +" "+ str(self.__buying_price) +" "+ str(self.__rent_price)


home1 = Home("hangev", 30, 5000, 1200000)
home2 = Home("alilah", 17, 4000, 1000000)

print(home2.tshua())

#3
class Cats:
    def __init__(self, name, age, color):
        self.__name = name
        self.__age = age
        self.__color = color

    def getname(self):
        return self.__name

    def setname(self, name):
        self.__name = name

    def getage(self):
        return self.__age

    def setage(self, age):
        self.__age = age

    def getcolor(self):
        return self.__color

    def setcolor(self, color):
        self.__color = color

    def sound(self):
        return ("meow")

    def mustache(self):
        return("the cat have a mustache")

    def __str__(self):
        return self.__name +" "+ str(self.__age) +" "+ self.__color

class Dogs:
    def __init__(self, name, breed, color):
        self.__name = name
        self.__breed = breed
        self.__color = color

    def getbreed(self):
        return self.__breed

    def setname(self, breed):
        self.__breed = breed

    def getage(self):
        return self.__age

    def setage(self, age):
        self.__age = age

    def getcolor(self):
        return self.__color

    def setcolor(self, color):
        self.__color = color

    def sound(self):
        return ("havhav")

    def bites(self):
        return("the dog bites")

    def __str__(self):
        return self.__name + " " + self.__breed + " " + self.__color

cat1 = Cats("mizi", 7, "black")
cat2 = Cats("pizi", 5, "white")
dog1 = Dogs("kika", "Belgian shepherd", "brown")
dog2 = Dogs("nala", "pitbull", "gray")

print(cat1, cat1.sound(), cat1.mustache())
print(cat2)
print(dog1, dog1.sound(), dog1.bites())
print(dog2)

#4
class Cars:
    def __init__(self, model, color, price):
        self.model = model
        self.__color = color
        self.__price = price

    def getModel(self):
        return self.model

    def setModel(self, model):
        self.model = model

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price

    def __str__(self):
        return self.model +" "+ self.__color +" "+str(self.__price)


car1 = Cars("Mazda", "Black", 30000)
car2 = Cars("Kia", "Red", 45000)
car3 = Cars("Hyundai", "white", 56000)
car4 = Cars("Hyundai", "green", 70000)

cars = [car1,car2,car3,car4]

def maxPrice():
    max = 0
    for i in range(len(cars)-1):
        if cars[i].getPrice() > cars[i+1].getPrice():
            max = cars[i]
        else:
            max = cars[i+1]
    return max

print(Cars.__str__(maxPrice()))
del car4.model
car4.setModel("number of wheels : 4")
print(car4)
print(car1)
print(car2)
print(car3)

#5
class Student:
    def __init__(self, name, id, mathGrade, histhoryGrade, literatureGrade, classs, yareOfBirht):
        self.__name = name
        self.__id = id
        self.__mathGrade = mathGrade
        self.__histhoryGrade = histhoryGrade
        self.__literatureGrade = literatureGrade
        self.__classs = classs
        self.__yaerOfBirht = yareOfBirht
        print(name + " is created!!")

    def getMathGrade(self):
        return self.__mathGrade

    def setMathGrade(self, mathgrade):
        self.__mathGrade = mathgrade

    def gethisthoryGrade(self):
        return self.__histhoryGrade

    def sethisthoryGrade(self, histhoryGrade):
        self.__histhoryGrade = histhoryGrade

    def getliteratureGrade(self):
        return self.__literatureGrade

    def setliteratureGrade(self, literatureGrade):
        self.__literatureGrade = literatureGrade

    def howOld(self):
          return 2022 - self.__yaerOfBirht

    def avg(self):
        avg = (self.__mathGrade+self.__histhoryGrade+self.__literatureGrade) // 3
        return avg

    def reguarDiploma(self):
        print("name of stident", self.__name + "\nstudent id is : ", self.__id)

    def gradeDiploma(self):
        print("math grade", str(self.__mathGrade),"\nhistory grade", str(self.__histhoryGrade), "\nliterature grade", str(self.__literatureGrade)+"\navg", self.avg())
        print()
        if self.avg() > 90:
            print("excellent!!!!")
        elif self.avg() < 60:
            print("not pass :( ")


    def __str__(self):
        return self.__name +" "+ str(self.__id) +" "+ str(self.__mathGrade) +" "+ str(self.__histhoryGrade) +" "+ str(self.__literatureGrade) +" "+ self.__classs +" "+ str(self.__yaerOfBirht)


st1 = Student("aviva", 555, 90, 100, 85, "QA", 1991)
st2 = Student("betty", 444, 100, 95, 70, "QA", 1999)
st3 = Student("rivka", 333, 88, 99, 70, "QA", 1994)
st4 = Student("tziona", 777, 100, 80, 85, "QA", 1994)
st5 = Student("daniel", 111, 30, 40, 35, "QA", 1994)

mystudent = [st1, st2, st3, st4,st5]

def maxavg():
    max = 0
    for i in range(len(mystudent)-1):
        if mystudent[i].avg() > mystudent[i+1].avg():
            max = mystudent[i]
        else:
            max = mystudent[i+1]
    return max


st1.reguarDiploma(), st1.gradeDiploma()
st2.reguarDiploma(), st2.gradeDiploma()
st3.reguarDiploma(), st3.gradeDiploma()
st4.reguarDiploma(), st4.gradeDiploma()
st5.reguarDiploma(), st5.gradeDiploma()

print(Student.__str__(maxavg()))



