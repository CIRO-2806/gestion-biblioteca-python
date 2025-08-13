import json


class Persona:
    def __init__(self,nombre,apellido,dni,edad,email):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._edad = edad
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
        
    def getEdad(self):
        return self._edad
    
    def setEdad(self,new_edad):
        self._edad = new_edad
        
    def getEmail(self):
        return self._email
    
    def setEmail(self,new_email):
        self._email = new_email
        
    def to_dict(self):
        return {
            "nombre": self._nombre,
            "apellido": self._apellido,
            "dni": self._dni,
            "edad": self._edad,
            "email": self._email
        }
    
    @classmethod
    def from_dict(cls,data):
        return cls(
            data["nombre"],
            data["apellido"],
            data["dni"],
            data["edad"],
            data["email"]
        )
        
    def guardarPersonas(persona, ARCHIVO_PERSONAS):
        with open(ARCHIVO_PERSONAS,"w", encoding="utf-8") as file:
            json.dump([per.to_dict() for per in persona], file, ensure_ascii=False, indent=4)
        print(f"Lista de personas guardada en {ARCHIVO_PERSONAS}")
    
    def cargarPersonas(ARCHIVO_PERSONAS):
        try:
            with open(ARCHIVO_PERSONAS,"r",encoding="utf-8") as file:
                data = json.load(file)
                return[Persona.from_dict(item) for item in data]
        except FileNotFoundError:
            return []


        