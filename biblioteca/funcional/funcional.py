from biblioteca.modelo.persona import Persona
from biblioteca.modelo.estudiante import Estudiante
from biblioteca.modelo.profesor import Profesor
from biblioteca.modelo.libro import Libro
from biblioteca.modelo.prestamo import Prestamo
from biblioteca.main import ARCHIVO_PERSONAS,ARCHIVO_PROFESORES,ARCHIVO_LIBROS,ARCHIVO_ESTUDIANTES,ARCHIVO_PRESTAMOS
from datetime import datetime

persona = Persona.cargarPersonas(ARCHIVO_PERSONAS)
profesor = Profesor.cargarProfesor(ARCHIVO_PROFESORES)
libro = Libro.cargarLibro(ARCHIVO_LIBROS)
estudiante = Estudiante.cargarEstudiante(ARCHIVO_ESTUDIANTES)
prestamo = Prestamo.cargarPrestamo(ARCHIVO_PRESTAMOS)

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
        persona = Persona.guardarPersonas(persona,ARCHIVO_PERSONAS)
        
        
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
        Persona.guardarPersonas(persona,ARCHIVO_PERSONAS)
        print("Persona Eliminada con éxito.")



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
        Estudiante.guardarEstudiante(estudiante,ARCHIVO_ESTUDIANTES)
        
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
                Estudiante.guardarEstudiante(estudiante,ARCHIVO_ESTUDIANTES)
                
    def eliminarEstudiante(estudiante):
        indice = int(input("Ingrese el indice del estudiante a eliminar: "))
        estudiante.pop(indice)
        Estudiante.guardarEstudiante(estudiante,ARCHIVO_ESTUDIANTES)
        print("Estudiante eliminado correctamente.")
        

class GestorLibros:
    def añadirLibro(libro):
        print("Agregar libro")
        nombre = input("Ingrese el nombre del libro: ")
        autor = input("Ingrese el autor del libro: ")
        isbn = int(input("Ingrese el isbn del libro: "))
        editorial = input("Ingrese el editorial del libro: ")
        año = input("Ingrese el año del libro: ")
        estado = "Disponible"
        nuevo_libro = Libro(nombre,autor,isbn,editorial,año,estado)
        libro.append(nuevo_libro)
        print("libro añadida correctamente")
        Libro.guardarLibro(libro,ARCHIVO_LIBROS)
        
    def listarLibro(libro):    
        print("Listar libros")
        if not libro:
            print("No hay libros registrados")
        else:
            r = 0
            for idx,lib in enumerate(libro):
                print(f"\nlibro Nº{idx} con índice {idx}")
                print("Nombre: ", lib.getNombre(),"\nAutor: ", lib.getAutor(), "\nIsbn: ", lib.getIsbn(), "\nEditorial: ", lib.getEditorial(), "\nAño: ", lib.getAño(), "\nEstado: ", lib.getEstado()) 

        
    def modificarLibro(libro):
        indice = int(input("Ingrese el índice del libro a modificar: "))
        for idx,lib in enumerate(libro):
            if idx == indice:
                print(f"Modificando al libro: {lib.getNombre()} de: {lib.getAutor()}")
                new_nombre = input("Ingrese el nuevo nombre: ")
                new_autor = input("Ingrese el nuevo autor:")
                new_isbn = int(input("Ingrese el nuevo isbn: "))
                new_editorial = input("Ingrese el nuevo editorial: ")
                new_año = input("Ingrese el nuevo año: ")
                
                lib.setNombre(new_nombre)
                lib.setAutor(new_autor)
                lib.setIsbn(new_isbn)
                lib.setEditorial(new_editorial)
                lib.setAño(new_año)
                print("libro modificado correctamente...")
                Libro.guardarLibro(libro, ARCHIVO_LIBROS)
                
    def eliminarLibro(libro):
        indice = int(input("Ingrese el indice del libro a eliminar: "))
        libro.pop(indice)
        Libro.guardarLibro(libro,ARCHIVO_ESTUDIANTES)
        print("Libro eliminado correctamente.")
    
    
class GestorProfesores:
    def añadirProfesor(profesor):
        print("Agregar profesor")
        nombre = input("Ingrese el nombre del profesor: ")
        apellido = input("Ingrese el apellido del profesor: ")
        dni = int(input("Ingrese el dni del profesor: "))
        materia = input("Ingrese la/s materia/s del profesor: ")
        email = input("Ingrese el email del profesor: ")
        
        nuevo_profesor = Profesor(nombre,apellido,dni,materia,email)
        profesor.append(nuevo_profesor)
        print("profesor añadido correctamente")
        profesor = Profesor.guardarProfesor(profesor, ARCHIVO_PROFESORES)
        
        
        
    def listarProfesor(profesor):    
        print("Listar profesores")
        if not profesor:
            print("No hay profesores registrados")
        else:
            r = 0
            for pro in profesor:
                r += 1
                print(f"\nprofesor Nº{r} con índice {r - 1}")
                print("Nombre: ", pro.getNombre(),"\nApellido: ", pro.getApellido(), "\nDni: ", pro.getDni(), "\nMaterias: ", pro.getMateria(), "\nEmail ", pro.getEmail())    

        
    def modificarProfesor(profesor):
        indice = int(input("Ingrese el índice del profesor a modificar: "))
        for idx,pro in enumerate(profesor):
            if idx == indice:
                print(f"Modificando al profesor: {pro.getNombre()} {pro.getApellido()}")
                new_nombre = input("Ingrese el nuevo nombre: ")
                new_apellido = input("Ingrese el nuevo apellido:")
                new_dni = int(input("Ingrese el nuevo dni: "))
                new_materia = input("Ingrese la/s nuevas materias: ")
                new_email = input("Ingrese el nuevo email: ")
                
                
                pro.setNombre(new_nombre)
                pro.setApellido(new_apellido)
                pro.setDni(new_dni)
                pro.setMateria(new_materia)
                pro.setEmail(new_email)
                print("profesor modificado correctamente...")
                Profesor.guardarProfesor(profesor, ARCHIVO_PROFESORES)
    def eliminarProfesor(profesor):
        indice = int(input("Ingrese el indice del profesor a eliminar: "))
        profesor.pop(indice)
        Profesor.guardarProfesor(profesor,ARCHIVO_PROFESORES)
        print("profesor eliminado correctamente.")
        
class GestorPrestamos:
    def registrarPrestamo(prestamo,libro):
        indicePrestado = int(input("Ingrese índice del libro a prestar: "))
        fechaPrestamo = datetime.now().strftime("%H:%M:%S, %d/%m/%Y")
        fechaDevolucion = "No devuelto."
        prestador = input("Ingrese el profesor que presta el libro: ")
        prestado = input("Ingrese a qué alumno será prestado el libro: ")
        for idx,lib in enumerate(libro):
            if idx == indicePrestado:
                libroPrestado = lib.getNombre()
                nuevo_prestamo = Prestamo(idx,libroPrestado,fechaPrestamo,fechaDevolucion,prestador,prestado)
                prestamo.append(nuevo_prestamo)
                Prestamo.guardarPrestamo(prestamo,ARCHIVO_PRESTAMOS)
                lib.setEstado("Prestado")
                
                

        print("Prestamo registrado con éxito")
    
    def listarPrestamo(prestamo):
        if not prestamo:
            print("No hay libros prestados")
        else:
            for pre in prestamo:
                print(f"\nIndice del Libro: {pre.getIndice()}\nLibro Prestado: {pre.getLibroPrestado()} \nFecha Prestamo: {pre.getFechaPrestamo()} \nFecha Devolución: {pre.getFechaDevolucion()} \nPrestado por: {pre.getPrestador()} \nPrestado a: {pre.getPrestado()}")
                
    def registrarDevolucion(prestamo,libro):
        indice = int(input("Ingrese el índice del libro a devolver: "))
        
        for idx,lib in enumerate(libro):
            if idx == indice:
                print(f"Libro a devolver: {lib.getNombre()}")
                op = input("Es correcto el libro? (S/N): ")
                if op == 'S':
                    lib.setEstado("Disponible")
                    
                    for pre in prestamo:
                        if pre.getIndice() == idx:
                            prestamo.remove(pre)
                        else:
                            print("Error")
                            break
                    print("Libro Devuelto con éxito.")
                    Libro.guardarLibro(libro,ARCHIVO_LIBROS)
                    Prestamo.guardarPrestamo(prestamo, ARCHIVO_PRESTAMOS)
                else:
                    break
            else:
                print("Error, índice de libro fuera de rango.")