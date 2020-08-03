from person.Person import Person

class Student(Person):

    def __init__(self, name, age):
        
        Person.__init__(self, name, age)