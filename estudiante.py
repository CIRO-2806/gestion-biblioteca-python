from persona import Persona

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