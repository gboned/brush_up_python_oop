from person.Person import Person

class Teacher(Person):

    def __init__(self, name, age, patience):
        super().__init__(name, age)
        self.patience = patience

    

    def getPatience(self):
        return self.patience


    def setPatience(self, newPatience):
        self.patience = newPatience