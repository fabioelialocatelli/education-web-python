class Disponibilidad(object):
    
    def __init__(self):
        self.cursos = ["C++", "Java", "Python", "SQL"]

    def curso(self, micurso):
        if micurso in self.cursos:
            return True
        else:
            return False

class Persona(object):

    def __init__(self, miNIF, minombre, misapellidos):
        self.NIF = miNIF
        self.nombre = minombre
        self.apellidos = misapellidos

    def __str__(self):
        return self.NIF + ": " + self.apellidos + ", " + self.nombre

class Alumno(Persona):

    def __init__(self, miNIF, minombre, misapellidos, micurso):
        super(Alumno, self).__init__(miNIF, minombre, misapellidos)
        self.curso = micurso
        self.disponible = Disponibilidad().curso(micurso)

    def __str__(self):
        return self.NIF + ": " + self.apellidos + ", " + self.nombre + " (curso: " + self.curso + ")"

persona = Persona("31101991R", "Jerome", "Harkonnen")
alumno1 = Alumno("24071937F", "Anna", "Picazo", "AJAX")
alumno2 = Alumno("11101929W", "Salvador", "Giorgetti", "SQL")
alumno3 = Alumno("08011953Q", "Erasmus", "Locatelli", "Python")

print(persona)

print(alumno1)
if(alumno1.disponible):
    print("Curso Disponible")
else:
    print("Curso no Disponible")

print(alumno2)
if(alumno2.disponible):
    print("Curso Disponible")
else:
    print("Curso no Disponible")

print(alumno3)
if(alumno3.disponible):
    print("Curso Disponible")
else:
    print("Curso no Disponible")
