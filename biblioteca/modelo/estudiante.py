from biblioteca.modelo.persona import Persona
import json

class Estudiante(Persona):
    def __init__(self,nombre,apellido,dni,edad,email,carrera,legajo):
        super().__init__(nombre,apellido,dni,edad,email)
        self._carrera = carrera
        self._legajo = legajo
        
        
    def getCarrera(self):
        return self._carrera
    
    def setCarrera(self,new_carrera):
        self._carrera = new_carrera
    
    def getLegajo(self):
        return self._legajo
    
    def setLegajo(self,new_legajo):
        self._legajo = new_legajo
        
    def to_dict(self):
        return {
            "nombre": self._nombre,
            "apellido": self._apellido,
            "dni": self._dni,
            "edad": self._edad,
            "email": self._email,
            "carrera": self._carrera,
            "legajo": self._legajo,
        }
    
    @classmethod
    def from_dict(cls,data):
        return cls(
            data["nombre"],
            data["apellido"],
            data["dni"],
            data["edad"],
            data["email"],
            data["carrera"],
            data["legajo"]
        )
        
    def guardarEstudiante(estudiante, ARCHIVO_ESTUDIANTES):
        with open(ARCHIVO_ESTUDIANTES,"w", encoding="utf-8") as file:
            json.dump([est.to_dict() for est in estudiante], file, ensure_ascii=False, indent=4)
        print(f"Lista de estudiantes guardada en {ARCHIVO_ESTUDIANTES}")
    
    def cargarEstudiante(ARCHIVO_ESTUDIANTES):
        try:
            with open(ARCHIVO_ESTUDIANTES,"r",encoding="utf-8") as file:
                data = json.load(file)
                return[Estudiante.from_dict(item) for item in data]
        except FileNotFoundError:
            return []