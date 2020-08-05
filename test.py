from person.Person import Person
from student.Student import Student
from teacher.Teacher import Teacher

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



def testStudent():

    studentInstance = Student('Noelia', 24)
    assert studentInstance.greet() == 'Hello my name is Noelia'



def testTeacher():

    teacherInstance = Teacher('Roger', 42, 0)
    assert teacherInstance.getName() == 'Roger'

    assert teacherInstance.getAge() == 42
    
    assert teacherInstance.getPatience() == 0

if __name__ == '__main__':
    testPerson()
    testStudent()