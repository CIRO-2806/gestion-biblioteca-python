from persona import Persona
from estudiante import Estudiante
def main():
    try:
        persona = [Persona("Ciro","Cabral","47339957","19","cirocabral2806@gmail.com"), Persona("Ana","Carrasco","1","36","ana@gmail.com")]
        estudiante = []
        opcion = 0

        while opcion != 99:
            print("----Personas----")
            print("Opcion 1 - Añadir Personas ")
            print("Opcion 2 - Listar Personas ")
            print("Opcion 3 - Modificar Personas ")
            print("Opcion 4 - Eliminar Personas ")
            print("Opcion 5 - Añadir Estudiantes ")
            print("Opcion 6 - Listar Estudiantes ")
            print("Opcion 7 - Modificar Estudiantes ")
            print("Opcion 8 - Eliminar Estudiantes ")
            
            opcion = int(input("Ingrese su opción, 99 para salir: "))

            match opcion:
                case 1:
                    GestorPersonas.añadirPersona(persona)
                case 2:
                    GestorPersonas.listarPersona(persona)
                case 3:
                    GestorPersonas.modificarPersona(persona)
                case 4:
                    GestorPersonas.eliminarPersona(persona)
                case 5:
                    GestorEstudiantes.añadirEstudiante(estudiante)
                case 6:
                    GestorEstudiantes.listarEstudiante(estudiante)
                case 7:
                    GestorEstudiantes.modificarEstudiante(estudiante)
                case 8:
                    GestorEstudiantes.eliminarEstudiante(estudiante)
                    

                
        print("Saliendo del programa...")
    except(ValueError):
        pass
    
    
class GestorPersonas:

    def añadirPersona(persona):
        print("Agregar personas")
        nombre = input("Ingrese el nombre de la persona: ")
        apellido = input("Ingrese el apellido de la persona: ")
        dni = int(input("Ingrese el dni de la persona: "))
        edad = int(input("Ingrese el edad de la persona: "))
        email = input("Ingrese el email de la persona: ")
        nueva_persona = Persona(nombre,apellido,dni,edad,email)
        persona.append(nueva_persona)
        print("Persona añadida correctamente")
        
    def listarPersona(persona):    
        print("Listar Personas")
        if not persona:
            print("No hay personas registradas")
        else:
            r = 0
            for per in persona:
                r += 1
                print(f"\nPersona Nº{r} con índice {r - 1}")
                print("Nombre: ", per.getNombre(),"\nApellido: ", per.getApellido(), "\nDni: ", per.getDni(), "\nEdad: ", per.getEdad(), "\nEmail ", per.getEmail(),  )    

        
    def modificarPersona(persona):
        indice = int(input("Ingrese el índice de la persona a modificar: "))
        for idx,per in enumerate(persona):
            if idx == indice:
                print(f"Modificando a la persona: {per.getNombre()} {per.getApellido()}")
                new_nombre = input("Ingrese el nuevo nombre: ")
                new_apellido = input("Ingrese el nuevo apellido:")
                new_dni = int(input("Ingrese el nuevo dni: "))
                new_edad = int(input("Ingrese la nueva edad: "))
                new_email = input("Ingrese el nuevo email: ")
                
                per.setNombre(new_nombre)
                per.setApellido(new_apellido)
                per.setDni(new_dni)
                per.setEdad(new_edad)
                per.setEmail(new_email)
                print("Persona modificada correctamente...")
                
    def eliminarPersona(persona):
        indice = int(input("Ingrese el indice de la persona a eliminar: "))
        persona.pop(indice)
        print("Persona Eliminada con éxito.")


# Estudiantes 

class GestorEstudiantes:
    def añadirEstudiante(estudiante):
        print("Agregar estudiantes")
        nombre = input("Ingrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
        dni = int(input("Ingrese el dni del estudiante: "))
        edad = int(input("Ingrese el edad del estudiante: "))
        email = input("Ingrese el email del estudiante: ")
        carrera = input("Ingrese la carrera del estudiante: ")
        legajo = input("Ingrese el legajo del estudiante: ")
        nuevo_estudiante = Estudiante(nombre,apellido,dni,edad,email,carrera,legajo)
        estudiante.append(nuevo_estudiante)
        print("Estudiante añadida correctamente")
        
    def listarEstudiante(estudiante):    
        print("Listar Estudiantes")
        if not estudiante:
            print("No hay estudiantes registrados")
        else:
            r = 0
            for est in estudiante:
                r += 1
                print(f"\nEstudiante Nº{r} con índice {r - 1}")
                print("Nombre: ", est.getNombre(),"\nApellido: ", est.getApellido(), "\nDni: ", est.getDni(), "\nEdad: ", est.getEdad(), "\nEmail: ", est.getEmail(),"\nCarrera:  ", est.getCarrera(), "\nLegajo: ", est.getLegajo())    

        
    def modificarEstudiante(estudiante):
        indice = int(input("Ingrese el índice del estudiante a modificar: "))
        for idx,est in enumerate(estudiante):
            if idx == indice:
                print(f"Modificando al estudiante: {est.getNombre()} {est.getApellido()}")
                new_nombre = input("Ingrese el nuevo nombre: ")
                new_apellido = input("Ingrese el nuevo apellido:")
                new_dni = int(input("Ingrese el nuevo dni: "))
                new_edad = int(input("Ingrese la nueva edad: "))
                new_email = input("Ingrese el nuevo email: ")
                new_carrera = input("Ingrese la nueva carrera: ")
                new_legajo = input("Ingrese el nuevo legajo: ")
                
                est.setNombre(new_nombre)
                est.setApellido(new_apellido)
                est.setDni(new_dni)
                est.setEdad(new_edad)
                est.setEmail(new_email)
                est.setCarrera(new_carrera)
                est.setLegajo(new_legajo)
                print("Estudiante modificado correctamente...")
                
    def eliminarEstudiante(estudiante):
        indice = int(input("Ingrese el indice del estudiante a eliminar: "))
        for idx,est in enumerate(estudiante):
            if idx == indice:
                est.pop()
                print("Estudiante eliminado correctamente.")


main()