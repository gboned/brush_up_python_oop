from person.Person import Person
#from student.Student import Student
#from teacher.Teacher import Teacher

def main():

    # Creamos una instancia de Persona
    p1 = Person('John', 36)

    # Obtenemos los atributos de la instancia
    print(p1.name) # John
    print(p1.age) # 36

    # Ejecutamos la función greet() de la clase Persona
    print(p1.greet()) # Hello my name is John

    # Usamos get para obtener el atributo name
    print('The created person name is ' + p1.getName() + ' at the beginning')
    
    # Usamos set para modificar el atributo name
    p1.setName('Marta')
    print('Now the name changed to ' + p1.getName())

    # __rpr__ devuelve la info de la instancia en formato string
    print(p1.__repr__()) 

    # __str__ muestra en pantalla la info de la instancia
    print(p1.__str__())


    # # Creamos una instancia de Student, heredera de Person
    # s1 = Student('Noelia', 24)
    # # Comprobamos que podemos usar los métodos de Person
    # s1.greet()


    # # Creamos una instancia de Teacher, heredera de Person 
    # t1 = Teacher('Roger', 42, 0)
    
    # # Comprobamos que podemo usar los métodos de Person...
    # print("The teacher's name is: " + t1.getName())

    # # y que también se pueden usar métodos propios de Teacher
    # print('And his patience is: ' + str(t1.get_patience()))


if __name__ == '__main__':
    main()