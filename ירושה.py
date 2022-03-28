class Person:
    def __init__(self,name,id):
        self.__name=name
        self.__id=id

    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name=name

    def getId(self):
        return self.__id

    def setId(self,id):
        self.__id=id

    def __str__(self):
        return self.__name+" "+str(self.__id)

    def makeVoice(self):
        print("waseeeeweew")


class Student(Person):

    def __init__(self,name,id,grade):
        super().__init__(name,id)
        self.__grade=grade

    def getGrade(self):
        return self.__grade

    def setGrade(self,grade):

        self.__grade=grade

    def __str__(self):
        return super().__str__()+" "+str(self.__grade)


st1=Student("ron",12222,80)
print(st1)
per1=Person("david",11111)
print(per1)

#Class exercises:

