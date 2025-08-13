from biblioteca.funcional.funcional import *
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_PERSONAS = os.path.join(BASE_DIR,"persona.json")
ARCHIVO_ESTUDIANTES =os.path.join(BASE_DIR, "estudiante.json")
ARCHIVO_LIBROS =os.path.join(BASE_DIR, "libro.json")
ARCHIVO_PROFESORES =os.path.join(BASE_DIR, "profesor.json")
ARCHIVO_PRESTAMOS =os.path.join(BASE_DIR, "prestamo.json")




def main():
    try:

        opcion = 0

        while opcion != 99:
            print("----Biblioteca----")
            print("Opción 1 - Añadir Personas ")
            print("Opción 2 - Listar Personas ")
            print("Opción 3 - Modificar Personas ")
            print("Opción 4 - Eliminar Personas ")
            print("Opción 5 - Añadir Estudiantes ")
            print("Opción 6 - Listar Estudiantes ")
            print("Opción 7 - Modificar Estudiantes ")
            print("Opción 8 - Eliminar Estudiantes ")
            print("Opción 9 - Añadir Profesores ")
            print("Opción 10 - Listar Profesores ")
            print("Opción 11 - Modificar Profesores ")
            print("Opción 12 - Eliminar Profesores ")
            print("Opción 13 - Añadir Libro")
            print("Opción 14 - Listar Libros")
            print("Opción 15 - Modificar Libros")
            print("Opción 16 - Eliminar Libros")
            print("Opción 17 - Registrar Prestamo")
            print("Opción 18 - Registrar devolución")
            print("Opción 19 - Listar Libros Prestados")


            
            opcion = int(input("Ingrese su opción, 99 para salir: " )) 

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
                case 9:
                    GestorProfesores.añadirProfesor(profesor)
                case 10:
                    GestorProfesores.listarProfesor(profesor)
                case 11:
                    GestorProfesores.modificarProfesor(profesor)
                case 12:
                    GestorProfesores.eliminarProfesor(profesor)
                case 13:
                    GestorLibros.añadirLibro(libro)
                case 14:
                    GestorLibros.listarLibro(libro)
                case 15:
                    GestorLibros.modificarLibro(libro)
                case 16:
                    GestorLibros.eliminarLibro(libro)
                case 17:
                    GestorPrestamos.registrarPrestamo(prestamo,libro)
                case 18:
                    GestorPrestamos.registrarDevolucion(prestamo,libro)
                case 19:
                    GestorPrestamos.listarPrestamo(prestamo)
                    
                
        print("Saliendo del programa...")
    except(ValueError):
        print("Error, ingresó un valor erróneo.")
    
    

if __name__ == "__main__":
    main()