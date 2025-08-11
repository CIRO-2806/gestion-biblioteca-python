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
    
    


        