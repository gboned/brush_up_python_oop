from person.Person import Person

class Teacher(Person):

    def __init__(self, name, age, patience):
        super().__init__(self, name, age)
        self.patience = patience