import json
from biblioteca.main import ARCHIVO_PROFESORES

class Profesor():
    def __init__(self,nombre,apellido,dni,materia,email):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._materia = materia
        self._email = email
        
    def getNombre(self):
        return self._nombre
    
    def setNombre(self,new_nombre):
        self._nombre = new_nombre    

    def getApellido(self):
        return self._apellido
    
    def setApellido(self,new_apellido):
        self._apellido = new_apellido   
        
    def getDni(self):
        return self._dni
    
    def setDni(self,new_dni):
        self._dni = new_dni
        
    def getMateria(self):
        return self._materia
    
    def setMateria(self,new_materia):
        self._materia = new_materia
        
    def getEmail(self):
        return self._email
    
    def setEmail(self,new_email):
        self._email = new_email
        
        
    def to_dict(self):
        return {
            "nombre": self._nombre,
            "apellido": self._apellido,
            "dni": self._dni,
            "materia": self._materia,
            "email": self._email
        }
    
    @classmethod
    def from_dict(cls,data):
        return cls(
            data["nombre"],
            data["apellido"],
            data["dni"],
            data["materia"],
            data["email"]
        )
        
    def guardarProfesor(profesor, ARCHIVO_PROFESORES):
        with open(ARCHIVO_PROFESORES,"w", encoding="utf-8") as file:
            json.dump([pro.to_dict() for pro in profesor], file, ensure_ascii=False, indent=4)
        print(f"Lista de Profesores guardada en {ARCHIVO_PROFESORES}")
    
    def cargarProfesor(ARCHIVO_PROFESORES):
        try:
            with open(ARCHIVO_PROFESORES,"r",encoding="utf-8") as file:
                data = json.load(file)
                return[Profesor.from_dict(item) for item in data]
        except FileNotFoundError:
            return []