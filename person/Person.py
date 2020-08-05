class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def greet(self):
        return 'Hello my name is ' + self.name



    def getName(self):
        return self.name
    

    def setName(self, newName):
        self.name = newName



    def getAge(self):
        return self.age


    def setAge(self, newAge):
        self.age = newAge



    def __repr__(self):
        personDict = {}
        personDict['name'] = self.name
        personDict['age'] = self.age
        return personDict

    def __str__(self):
        personDictStr = "{'name': '" + self.name + "', 'age': " + str(self.age) + "}"
        return personDictStr