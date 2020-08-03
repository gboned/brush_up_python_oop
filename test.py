from person.Person import Person

def testPerson():

    johnInstance = Person('John', 36)

    # Comprobar que no esté vacío
    assert johnInstance != None
    assert johnInstance.name == 'John'
    assert johnInstance.age == 36

    assert johnInstance.greet() == 'Hello my name is John'
     
    assert johnInstance.getName() == 'John'
    johnInstance.setName('Marta')
    assert johnInstance.getName() == 'Marta'

    assert johnInstance.getAge() == 36

    dictMarta = johnInstance.__repr__()
    assert dictMarta['name'] == 'Marta'
    assert dictMarta['age'] == 36

if __name__ == '__main__':
    testPerson()